# coding=utf-8

import nltk
from nltk.tokenize import sent_tokenize, word_tokenize

nltk.download('punkt')

"""
标记字符串(分词器/标记器) -> 按照句子/单词来分词
"""

source = "Trend Micro Titanium allows you to protect a limited number of devices. Installing this protection on your Android device will count towards that limit. Google Play is a trademark of Google Inc. Amazon, Kindle, Kindle Fire, the Amazon Kindle logo and the Kindle Fire logo are trademarks of Amazon.com, Inc. or its affiliates."
source = '你好啊！我是孔昀晖。你好吗？我想说：“我喜欢你！”'
source = '你好啊! 我是孔昀晖. 你好吗? 我想说："我喜欢你! "'  # 全角字符替换，并给空格（英文句子就是会有空格），分句可行！

# 句子分词
sentences = sent_tokenize(source)  # 默认language='english'。在 nltk_data/tokenizers/punkt/{}.pickle 下可以看到目前不支持中文
print(sentences)

# 单词分词
words = word_tokenize(source)
print(words)
