# coding=utf-8

# 参考：https://gist.github.com/shingchi/64c04e0dd2cbbfbc1350

# CJK_SCOPE = [
#     (int('4E00', 16), int('9FA5', 16)),  # 基本汉字
#     (int('1100', 16), int('11FF', 16)),  # 韩文字母
#     (int('3130', 16), int('318F', 16)),  # 韩文兼容字母
#     (int('AC00', 16), int('D7AF', 16)),  # 韩文拼音
# ]


CJK_SCOPE = [
    (int('4E00', 16), int('9FA5', 16)),
    (int('2E80', 16), int('A4CF', 16)),
    (int('F900', 16), int('FAFF', 16)),
    (int('FE30', 16), int('FE4F', 16)),
    (int('AC00', 16), int('D7AF', 16))
]

def is_CJK(text):
    for char in text:
        for CJK_START, CJK_END in CJK_SCOPE:
            if CJK_START <= ord(char) <= CJK_END:
                return True
    return False


print(is_CJK('It should never contain personal information.'))
