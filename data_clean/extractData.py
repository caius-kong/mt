# coding=UTF-8
import sys
import os


def get_args():
    try:
        tlang_code = sys.argv[1]
        if tlang_code is None or tlang_code == '':
            raise Exception
    except:
        print("##################### ERROR TIP ####################\n"
              "## Usage: extractData.py {tlang_code}##\n"
              "####################################################\n")
    return tlang_code


def match_fluent_sentence(line):
    if 8 <= len(line.split(' ')) <= 16:
        return True
    return False


def open_write_files(sfile_not_extract_path, tfile_not_extract_path, sfile_extract_path, tfile_extract_path):
    if os.path.exists(sfile_not_extract_path):
        os.remove(sfile_not_extract_path)
    if os.path.exists(tfile_not_extract_path):
        os.remove(tfile_not_extract_path)
    if os.path.exists(sfile_extract_path):
        os.remove(sfile_extract_path)
    if os.path.exists(tfile_extract_path):
        os.remove(tfile_extract_path)

    not_extract_sfile = open(sfile_not_extract_path, 'a', encoding='utf-8')
    not_extract_tfile = open(tfile_not_extract_path, 'a', encoding='utf-8')
    extract_sfile = open(sfile_extract_path, 'a', encoding='utf-8')
    extract_tfile = open(tfile_extract_path, 'a', encoding='utf-8')
    return not_extract_sfile, not_extract_tfile, extract_sfile, extract_tfile


def close_files(not_extract_sfile, not_extract_tfile, extract_sfile, extract_tfile):
    not_extract_sfile.close()
    not_extract_tfile.close()
    extract_sfile.close()
    extract_tfile.close()


# input params
# tlang_code = get_args()
tlang_code = 'fr'

sfile_path = 'output/all_en.align'
tfile_path = 'output/all_' + tlang_code + '.align'
not_extract_sfile_path = 'output/not_extract_en.txt'
not_extract_tfile_path = 'output/not_extract_' + tlang_code + '.txt'
extract_sfile_path = 'output/extract_en.txt'
extract_tfile_path = 'output/extract_' + tlang_code + '.txt'

# prepare
with open(sfile_path, 'r', encoding='utf-8') as f:
    slines = f.readlines()
with open(tfile_path, 'r', encoding='utf-8') as f:
    tlines = f.readlines()
not_extract_sfile, not_extract_tfile, extract_sfile, extract_tfile = open_write_files(not_extract_sfile_path,
                                                                                      not_extract_tfile_path,
                                                                                      extract_sfile_path,
                                                                                      extract_tfile_path)

# extract
extract_count = 0
for i in range(0, len(slines)):
    sline = slines[i]
    tline = tlines[i]
    if extract_count < 10000 and match_fluent_sentence(sline):
        extract_sfile.write(sline)
        extract_tfile.write(tline)
        extract_count += 1
    else:
        not_extract_sfile.write(sline)
        not_extract_tfile.write(tline)
close_files(not_extract_sfile, not_extract_tfile, extract_sfile, extract_tfile)
print('extract success!')
