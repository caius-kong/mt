# coding=utf-8
import json
import os
import uuid

import requests
import xlwt

#################################################
# 对比smt、nmt base、nmt custom、vender的翻译质量 #
#################################################

language_dict = {
    "zh": "zh-CN",
    "ja": "ja-JP"
}


def translate_from_smt(text, tlang_name):
    target = ''
    error_msg = ''
    smt_trans_result = requests.post('http://10.64.14.49:8080',
                                     json={"tlang_name": tlang_name, "text": text, "method": ["3"]})
    smt_trans_result_text_dict = json.loads(smt_trans_result.text)
    if smt_trans_result_text_dict['result'] != 0:
        target = smt_trans_result_text_dict['text']
    else:
        error_msg = smt_trans_result_text_dict['error']
    return target, error_msg


def translate_from_ms_nmt_init():
    global base_url, headers
    if 'TRANSLATOR_TEXT_KEY' in os.environ:
        subscriptionKey = os.environ['TRANSLATOR_TEXT_KEY']
    else:
        print('Environment variable for TRANSLATOR_TEXT_KEY is not set.')
        exit()

    base_url = 'https://api.cognitive.microsofttranslator.com'

    headers = {
        'Ocp-Apim-Subscription-Key': subscriptionKey,
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }


def translate_from_ms_nmt(text, tlang_code, category='general'):
    body = [{
        'text': text
    }]
    # to是必选参数，其他都可选。category指定部署的自定义翻译，默认general; textType指定是否作为html翻译，默认plain
    params = '&from=en&to=%s&textType=html&category=%s' % (tlang_code, category)
    request = requests.post(base_url + '/translate?api-version=3.0' + params, headers=headers, json=body)
    response = request.json()
    return response[0]['translations'][0]['text']


def setup_sheet_title(worksheet):
    style = xlwt.XFStyle()
    # 设置边框
    borders = xlwt.Borders()
    borders.left = xlwt.Borders.THIN
    borders.right = xlwt.Borders.THIN
    borders.top = xlwt.Borders.THIN
    borders.bottom = xlwt.Borders.THIN
    borders.left_colour = 0x40
    borders.right_colour = 0x40
    borders.top_colour = 0x40
    borders.bottom_colour = 0x40
    style.borders = borders
    # 设置对齐方式
    alignment = xlwt.Alignment()
    alignment.horz = xlwt.Alignment.HORZ_CENTER
    alignment.vert = xlwt.Alignment.VERT_CENTER
    style.alignment = alignment
    # 设置单元格背景色
    pattern = xlwt.Pattern()  # Create the Pattern
    pattern.pattern = xlwt.Pattern.SOLID_PATTERN  # May be: NO_PATTERN, SOLID_PATTERN, or 0x00 through 0x12
    pattern.pattern_fore_colour = 5
    style.pattern = pattern
    # 设置标题
    worksheet.write_merge(0, 1, 0, 0, 'type', style)
    worksheet.write_merge(0, 1, 1, 1, 'corpus', style)
    worksheet.write_merge(0, 1, 2, 2, 'score', style)


def update_worksheet_content(worksheet, row, src_line, smt_res, nmt_base_res, nmt_custom_res, tgt_line):
    # col1: type val
    worksheet.write(row, 0, label="source")
    worksheet.write(row + 1, 0, label="smt")
    worksheet.write(row + 2, 0, label="base nmt")
    worksheet.write(row + 3, 0, label="custom nmt")
    worksheet.write(row + 4, 0, label="target")
    # col2: corpus val
    worksheet.write(row, 1, label=src_line)
    worksheet.write(row + 1, 1, label=smt_res)
    worksheet.write(row + 2, 1, label=nmt_base_res)
    worksheet.write(row + 3, 1, label=nmt_custom_res)
    worksheet.write(row + 4, 1, label=tgt_line)


def len_byte(value):
    """
    获取字符串长度，一个中文的长度为2
    """
    length = len(value)
    utf8_length = len(value.encode('utf-8'))
    length = (utf8_length - length) / 2 + length
    return int(length)


def update_corpus_len_max(current_corpus_lens):
    global corpus_len_max
    for x in current_corpus_lens:
        if x > corpus_len_max:
            corpus_len_max = x


def self_adaptive_col_width(worksheet):
    global corpus_len_max
    worksheet.col(1).width = 256 * corpus_len_max if 256 * corpus_len_max < 65536 else 65535


# base params
tlang_code = 'ja'
custom_category = '0c9c6bb9-6d48-4855-9aab-5cf2e501acef-TECH'

# fetch txt
res_file_path_txt = 'output/translate_results.txt'
if os.path.exists(res_file_path_txt):
    os.remove(res_file_path_txt)
txt_file = open(res_file_path_txt, 'a', encoding='utf-8')

# fetch excel sheet and set title
res_file_path = 'output/translate_results.xls'
if os.path.exists(res_file_path):
    os.remove(res_file_path)
workbook = xlwt.Workbook(encoding='ascii')
worksheet = workbook.add_sheet('model translate contrasts')
setup_sheet_title(worksheet)

# ms nmt init
translate_from_ms_nmt_init()

# read data and translate by different model
with open('input/src-test3.txt', 'r', encoding='utf-8') as f:
    slines = f.readlines()
with open('input/tgt-test3.txt', 'r', encoding='utf-8') as f:
    tlines = f.readlines()
corpus_len_max = 0
row = 2
for i in range(0, len(slines)):
    src_line = slines[i].strip("\n")
    # smt_res, error_msg = translate_from_smt(src_line, language_dict.get(tlang_code))
    smt_res = "SMT"
    nmt_base_res = translate_from_ms_nmt(src_line, tlang_code)
    nmt_custom_res = translate_from_ms_nmt(src_line, tlang_code, category=custom_category)
    tgt_line = tlines[i].strip("\n")

    # 写入translate_results.txt
    txt_file.write(src_line + "\n" + smt_res + "\n" + nmt_base_res + "\n" + nmt_custom_res + "\n" + tgt_line + "\n\n")

    # 写入translate_results.xls
    update_worksheet_content(worksheet, row, src_line, smt_res, nmt_base_res, nmt_custom_res, tgt_line)
    row += 6
    update_corpus_len_max(
        (len_byte(src_line), len_byte(smt_res), len_byte(nmt_base_res), len_byte(nmt_custom_res), len_byte(tgt_line)))
    print("current progress: %s" % ("%.2f%%" % ((i + 1) / len(slines) * 100)))
self_adaptive_col_width(worksheet)
workbook.save('output/translate_results.xls')
