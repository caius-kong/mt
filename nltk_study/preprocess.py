# coding=utf-8

from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

"""
将数据转换成计算机可以理解的东西，这个过程称为"预处理"。
* 预处理的形式之一就是过滤掉无用的数据。在自然语言处理中，无用词（数据）被称为停止词。一个最常见的，非官方的，无用词的例子是单词umm。NLTK 用一堆他们认为是停止词的单词，来让你起步。
* 预处理的另一种形式是"词干提取(Stemming)"
"""

# 过滤停止词
source = "This is a sample sentence, showing off the stop words filtration."
stop_words = set(stopwords.words('english'))
words = word_tokenize(source)
filtered_words = [w for w in words if not w in stop_words]
print(words)
print(filtered_words)

# 提取词干
ps = PorterStemmer()  # 瓷感提取算法
source = "It is important to by very pythonly while you are pythoning with python. All pythoners have pythoned poorly at least once."
words = word_tokenize(source)
for w in words:
    print(ps.stem(w))
