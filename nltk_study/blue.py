# coding=utf-8
from nltk.translate.bleu_score import sentence_bleu, corpus_bleu

"""
计算句子/文档 bleu分数

知识：
1-gram 1元相同数   * weights=(1, 0, 0, 0)
2-gram 1~2元相同数 * weights=(0.5, 0.5, 0, 0)
3-gram 1~3元相同数 * weights=(0.33, 0.33, 0.33, 0)
4-gram 1~4元相同数 * weights=(0.25, 0.25, 0.25, 0.25)  ==>  默认bleu score = 累加的4-gram分数
"""

# 语句BLEU分数
reference = [['this', 'is', 'a', 'test'], ['this', 'is', 'a', 'test', '.']]  # 参考语句可以多句，取max(blue)
candidate = ['this', 'is', 'a', 'test', '.']
score = sentence_bleu(reference, candidate)
print(score)

# 语料库BLEU分数
references = [[['this', 'is', 'a', 'test']], [['how', 'old', 'are', 'you']]]
candidates = [['this', 'is', 'a', 'test'], ['how', 'old', 'are', 'you', '?']]
score = corpus_bleu(references, candidates)
print(score)
