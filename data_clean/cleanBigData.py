# coding=UTF-8
import re
import time

# for example: <tuv xml:lang="EN-US">
source_pattern = re.compile(r'<tuv xml:lang="EN-US">')
target_pattern = re.compile(r'<tuv xml:lang="FR-FR">')

file_path = 'old.tmx'


# 特大文件文件逐行处理。一般来说上G的文件就是特大文件，但是也是相对于机器而言，例如机器内存就256M, 那么100M对你来说就是特大文件
def get_total():
    """
    使用enumerate循环读取的方法,拿索引
    :return:
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        _count = -1
        for _count, _line in enumerate(f):
            pass
        _count += 1
    return _count


def get_line():
    """
    获取大块数据的yield函数
    :return:
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        for _line in f:
            yield _line


start_time = time.time()
start_row = 0
end_row = 1000
step = 1000
total = get_total()
gen = get_line()
while 1:
    lines = [next(gen) for i in range(start_row, end_row)]
    if not lines:
        break
    for i in range(0, len(lines)):
        line = lines[i]
        if source_pattern.match(line):
            if i + 1 > len(lines) - 1:
                continue
            source_line = lines[i + 1]
            source_content = re.sub(r"<[\W]?seg>", '', source_line)
            print('index:{}, source: {}'.format(i, source_content))
    start_row = end_row
    end_row = end_row + step if end_row + step < total else total
print(time.time() - start_time, "seconds")
