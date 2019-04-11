# coding=utf-8

import nltk
from nltk.tokenize import sent_tokenize, word_tokenize

nltk.download('punkt')

"""
标记字符串(分词器/标记器) -> 按照句子/单词来分词
"""

source = "Hello Mr. Smith, how are you doing today? The weather is great, and Python is awesome. The sky is pinkish-blue. You shouldn't eat cardboard."

# 句子分词
sentences = sent_tokenize(source)
print(sentences)

# 单词分词
words = word_tokenize(source)
print(words)
