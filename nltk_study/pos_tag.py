# coding=utf8
import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer

"""
Part of speech tagging(词性标注) - 把一个句子中的单词标注为名词，形容词，动词等

POS tag list:
CC  coordinating conjunction
CD  cardinal digit
DT  determiner
EX  existential there (like: "there is" ... think of it like "there exists")
FW  foreign word
IN  preposition/subordinating conjunction
JJ  adjective   'big'
JJR adjective, comparative  'bigger'
JJS adjective, superlative  'biggest'
LS  list marker 1)
MD  modal   could, will
NN  noun, singular 'desk'
NNS noun plural 'desks'
NNP proper noun, singular   'Harrison'
NNPS    proper noun, plural 'Americans'
PDT predeterminer   'all the kids'
POS possessive ending   parent's
PRP personal pronoun    I, he, she
PRP$    possessive pronoun  my, his, hers
RB  adverb  very, silently,
RBR adverb, comparative better
RBS adverb, superlative best
RP  particle    give up
TO  to  go 'to' the store.
UH  interjection    errrrrrrrm
VB  verb, base form take
VBD verb, past tense    took
VBG verb, gerund/present participle taking
VBN verb, past participle   taken
VBP verb, sing. present, non-3d take
VBZ verb, 3rd person sing. present  takes
WDT wh-determiner   which
WP  wh-pronoun  who, what
WP$ possessive wh-pronoun   whose
WRB wh-abverb   where, when
"""

# 1. 创建数据
train_text = state_union.raw("2005-GWBush.txt")
print(train_text)
sample_text = state_union.raw("2006-GWBush.txt")
# 2. 无监督机器训练（训练出特定的标记器）
custom_sent_tokenizer = PunktSentenceTokenizer(train_text)
# 3. 句子分词
tokenized = custom_sent_tokenizer.tokenize(sample_text)
# 4. 内容处理
try:
    for i in tokenized[:1]:
        # 单词切分
        words = nltk.word_tokenize(i)
        # 词性标注
        tagged = nltk.pos_tag(words)
        print(tagged)
        # 词汇分块（利用正则+词性）
        chunkGram = r"""Chunk_demo: {<RB.?>*<VB.?>*<NNP>+<NN>?}"""  # 解释：<RB.?>* = (RB + 非换行符(0~1)) * (0~n) = 零个或多个任何时态的副词
        chunkParser = nltk.RegexpParser(chunkGram)
        chunked = chunkParser.parse(tagged)
        for subtree in chunked.subtrees(filter=lambda t: t.label() == 'Chunk_demo'):
            print(subtree)
        chunked.draw()
except Exception as e:
    print(str(e))
