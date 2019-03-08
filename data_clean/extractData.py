# coding=UTF-8
import os
import re
import sys


def get_args():
    try:
        tlang_code = sys.argv[1]
        if tlang_code is None or tlang_code == '':
            raise Exception
    except:
        print("##################### ERROR TIP #####################\n"
              "## Usage: python3 extractData.py src_path tgt_path ##\n"
              "#####################################################\n")
    return tlang_code


def open_write_files(train_sfile_path, train_tfile_path, val_sfile_path, val_tfile_path, test_sfile_path,
                     test_tfile_path):
    if os.path.exists(train_sfile_path):
        os.remove(train_sfile_path)
    if os.path.exists(train_tfile_path):
        os.remove(train_tfile_path)
    if os.path.exists(val_sfile_path):
        os.remove(val_sfile_path)
    if os.path.exists(val_tfile_path):
        os.remove(val_tfile_path)
    if os.path.exists(test_sfile_path):
        os.remove(test_sfile_path)
    if os.path.exists(test_tfile_path):
        os.remove(test_tfile_path)

    train_sfile = open(train_sfile_path, 'a', encoding='utf-8')
    train_tfile = open(train_tfile_path, 'a', encoding='utf-8')
    val_sfile = open(val_sfile_path, 'a', encoding='utf-8')
    val_tfile = open(val_tfile_path, 'a', encoding='utf-8')
    test_sfile = open(test_sfile_path, 'a', encoding='utf-8')
    test_tfile = open(test_tfile_path, 'a', encoding='utf-8')
    return train_sfile, train_tfile, val_sfile, val_tfile, test_sfile, test_tfile


def close_files(train_sfile, train_tfile, val_sfile, val_tfile, test_sfile, test_tfile):
    train_sfile.close()
    train_tfile.close()
    val_sfile.close()
    val_tfile.close()
    test_sfile.close()
    test_tfile.close()


def match_fluent_sentence(line):
    match = re.match(r'[a-zA-Z\s,.-:]+', line)
    # 8~16个单词 && 仅由字母、空格、逗号，句号，短横，冒号组成
    if 8 <= len(line.split(' ')) <= 16 and match is not None and match.group() == line:
        return True
    return False


# input params
# tlang_code = get_args()
tlang_code = 'de'

# prepare
sfile_path = 'output/all_en.align'
tfile_path = 'output/all_' + tlang_code + '.align'
train_sfile_path = 'output/src-training.align'
train_tfile_path = 'output/tgt-training.align'
val_sfile_path = 'output/src-tuning.align'
val_tfile_path = 'output/tgt-tuning.align'
test_sfile_path = 'output/src-testing.align'
test_tfile_path = 'output/tgt-testing.align'
with open(sfile_path, 'r', encoding='utf-8') as f:
    slines = f.readlines()
with open(tfile_path, 'r', encoding='utf-8') as f:
    tlines = f.readlines()
train_sfile, train_tfile, val_sfile, val_tfile, test_sfile, test_tfile = open_write_files(train_sfile_path,
                                                                                          train_tfile_path,
                                                                                          val_sfile_path,
                                                                                          val_tfile_path,
                                                                                          test_sfile_path,
                                                                                          test_tfile_path)

# extract
extract_count = 0
for i in range(0, len(slines)):
    sline = slines[i]
    tline = tlines[i]
    if 0 <= extract_count < 5000 and match_fluent_sentence(sline):
        val_sfile.write(sline)
        val_tfile.write(tline)
        extract_count += 1
    elif 5000 <= extract_count < 10000 and match_fluent_sentence(sline):
        test_sfile.write(sline)
        test_tfile.write(tline)
        extract_count += 1
    else:
        train_sfile.write(sline)
        train_tfile.write(tline)
close_files(train_sfile, train_tfile, val_sfile, val_tfile, test_sfile, test_tfile)
print('extract success!')
