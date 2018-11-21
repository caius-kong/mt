# coding=UTF-8
import os
import re
import sys

language_dict = {
    "fr": "fr-FR",
    "de": "de-DE",
    "es": "es-ES",
    "ko": "ko-KR",
    "zh-TW": "zh-TW"
}


def get_args():
    try:
        tlang_code = sys.argv[1]
        input_folder = sys.argv[2]
        if (tlang_code is None or tlang_code == '') or (input_folder is None or input_folder == ''):
            raise Exception
    except:
        print("##################### ERROR TIP ####################\n"
              "## Usage: cleanData.py {tlang_code} {input_folder}##\n"
              "####################################################\n")
    return tlang_code, input_folder


def pre_handle(line):
    line = line.strip(' ')
    line = line.replace("&amp;", "&").replace("&amp;", "&").replace("&nbsp;", ' ').replace("&quot;", '"').replace(
        '&lt;', '<').replace('&gt;', '>').replace("&#xD;", " ").replace("\t", "")
    return line


def del_blank(s):
    return " ".join([x for x in s.split(" ") if x != ""])


def content_handle(content_line):
    content = seg_tag_pattern.sub('', content_line)
    if html_pattern.match(content):
        content = html_pattern.sub('', content).strip()
    if tr_pattern.match(content):
        content = tr_pattern.sub('', content).strip()
    content = html_tag_pattern.sub('', content)
    # if css_pattern.match(content):
    #     content = css_pattern.sub("", content).strip()
    return del_blank(content)


def init_file_path_list(root_dir):
    for lists in os.listdir(root_dir):
        path = os.path.join(root_dir, lists)
        file_path_list.append(path)
        if os.path.isdir(path):
            init_file_path_list(path)


def file_prepare():
    sfile_path = output_folder + "/all_en.align"
    tfile_path = output_folder + "/all_" + tlang_code + ".align"
    if os.path.exists(sfile_path):
        os.remove(sfile_path)
    if os.path.exists(tfile_path):
        os.remove(tfile_path)
    sfile = open(sfile_path, 'a', encoding='utf-8')
    tfile = open(tfile_path, 'a', encoding='utf-8')
    return sfile, tfile


def count_align_check(source_write_count, target_write_count, file_path):
    if source_write_count != target_write_count:
        print("ERROR: {} parse error: write count no align, please check parse rule".format(file_path))
        sys.exit(0)


def small_file_clean_data(file_path, sfile, tfile):
    """
    小文件逐行处理
    :return:
    """
    try:
        f = open(file_path, 'r', encoding='utf-8')
        lines_origin = f.readlines()
    except:
        f = open(file_path, 'r', encoding='utf-16')
        lines_origin = f.readlines()
    lines = list(map(pre_handle, lines_origin))
    source_write_count = 0
    target_write_count = 0
    source_content = ''
    target_content = ''
    for i in range(0, len(lines)):
        line = lines[i]
        if skip_file_pattern.match(line):
            break
        if source_pattern.match(line):
            target_content = ''
            source_line = lines[i + 1]
            source_content = content_handle(source_line)
        if target_pattern.match(line):
            target_line = lines[i + 1]
            target_content = content_handle(target_line)
        # 当本轮解析的st/tt同时有效时，写入
        if source_content != '' and source_content != '\n' and target_content != '' and target_content != '\n':
            sfile.write(source_content)
            source_write_count += 1
            tfile.write(target_content)
            target_write_count += 1
            # 清理本轮数据
            source_content = ''
            target_content = ''
    f.close()
    count_align_check(source_write_count, target_write_count, file_path)


# input params
# tlang_code, input_folder = get_args()
tlang_code = 'de'
input_folder = '/Users/caius_kong/Documents/work/2018/MT/TMX/de-DE/2018.11'

# match pattern
source_pattern = re.compile(r'<tuv xml:lang="EN-US">', re.IGNORECASE)
target_pattern_str = r'<tuv xml:lang="{}">'.format(language_dict.get(tlang_code))
target_pattern = re.compile(target_pattern_str, re.IGNORECASE)
skip_file_pattern = re.compile(r'<prop type="RTFFontTable">')
seg_tag_pattern = re.compile(r'<[/]?seg>')
html_tag_pattern = re.compile(r'</?\w+[^>]*>')
html_pattern = re.compile(r'<!DOCTYPE html>[\W\w]*</html>', re.IGNORECASE)
tr_pattern = re.compile(r'<tr[^>]*>[\W\w]*<[/]?tr[^>]*>')
# css_pattern =  re.compile(r'[\W\w]*{[\W\w]*}')

file_path_list = []
init_file_path_list(input_folder)
output_folder = os.path.join(os.getcwd(), "output")
sfile, tfile = file_prepare()
for file_path in file_path_list:
    if os.path.splitext(file_path)[1] != '.tmx':
        continue
    print("file parse: " + file_path)
    small_file_clean_data(file_path, sfile, tfile)
sfile.close()
tfile.close()
