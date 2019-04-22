# coding=utf-8

import jieba

""" 结巴中文分词：做最好的 Python 中文分词组件 """

# 分词
seg_gen = jieba.cut("你好啊！我是孔昀晖。你好吗？我想说：“我喜欢你！”")
print([seg for seg in seg_gen])
