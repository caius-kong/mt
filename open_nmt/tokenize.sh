#!/usr/bin/env bash

# 标记化的目标是将原始句子转换为标记序列。两个主要操作按顺序执行：
# 1、规范化 - 对源序列应用一些统一变换以识别和保护某些特定序列（例如url），规范化字符（例如所有类型的引号，unicode变体）甚至将某些变体（如日期）标准化为唯一表示更简单的翻译过程
# 2、标记化本身 - 将实际的标准化句子转换为空格分隔的标记序列以及可能的特征（案例）。

# Optional: -mode conservative                      (accepted: space, conservative, aggressive. 定义标记化的积极程度，aggressive只保留字母/数字序列，conservative允许混合使用字母数字，如"2,000", "E65", "soft-landing"等，space正在进行空间标记化)
# Optional: -case_feature false                     (Generate case feature. 论坛：一般情况下使用-case_feature对几乎所有语言都是一个好主意，并且在源中的目标案例变体中处理和呈现时表现出良好的性能。但是有人说反向bleu下降了-->需要实验)
# Optional: -joiner_annotate false                  (Include joiner annotation using -joiner character. If choose true, you can use detokenize.lua)
# Optional: -segment_alphabet <table>               (特殊语种（中日，单词间无空格）需要指定分割字母表。例如，将中文句子拆分为字符，使用 -segment_alphabet Han)
#th tools/tokenize.lua -mode aggressive -case_feature true -joiner_annotate true < file > file.tok
for f in input/en-de/* ; do th $OPENNMT_HOME/tools/tokenize.lua -mode aggressive -case_feature true -segment_case true -joiner_annotate true < $f > $f.tok ; done

# If you activate -joiner_annotate marker, the tokenization is reversible. Just use:
#th tools/detokenize.lua -mode aggressive -case_feature true -joiner_annotate true < file.tok > file.detok

# for example:
#wget "https://s3.amazonaws.com/opennmt-trainingdata/wmt15-de-en.tgz"
#tar xzf wmt15-de-en.tgz
#for f in ../wmt15-de-en/* ; do th tools/tokenize.lua -mode aggressive -case_feature true -joiner_annotate true < $f > $f.tok ; done
#for l in en de ; do cat ../wmt15-de-en/commoncrawl.de-en.$l.tok ../wmt15-de-en/europarl-v7.de-en.$l.tok ../wmt15-de-en/news-commentary-v10.de-en.$l.tok > ../wmt15-de-en/wmt15-all-de-en.$l.tok ; done
#th preprocess.lua -train_src ../wmt15-de-en/wmt15-all-de-en.en.tok -train_tgt ../wmt15-de-en/wmt15-all-de-en.de.tok -valid_src ../wmt15-de-en/newstest2013.en.tok -valid_tgt ../wmt15-de-en/newstest2013.de.tok -save_data ../wmt15-de-en/wmt15-all-en-de
#th train.lua -data ../wmt15-de-en/wmt15-all-en-de-train.t7 -save_model ../wmt15-de-en/wmt15-all-en-de -gpuid 1
#wget http://www.statmt.org/wmt15/dev-v2.tgz
#th translate.lua -model /path/to/trained/model/wmt15-all-en-de_epoch13_7.28.t7 -src /path/to/testset/newstest2014.en.tok -output pred.txt -gpuid 1


#参考：http://forum.opennmt.net/t/training-english-german-wmt15-nmt-engine/29


# 如何检查哪个时代产生最好的质量
#for f in ~/OpenNMT/endeproj/endeproj_model/endeproj_ende_nmt_model_epoch*.t7
#do
#  th translate.lua -model $f -src ~/OpenNMT/endeproj/endeproj_model/trans/tst_src.txt.tok -output ~/OpenNMT/endeproj/endeproj_model/trans/${f##*/}_MT.txt;
#  echo ~/OpenNMT/endeproj/endeproj_model/trans/${f##*/}_MT.txt >> ~/OpenNMT/endeproj/endeproj_model/trans/BLEU_scores.txt;
#  perl benchmark/3rdParty/multi-bleu.perl ~/OpenNMT/endeproj/endeproj_model/trans/test_tgt.txt.tok < ~/OpenNMT/endeproj/endeproj_model/trans/${f##*/}_MT.txt >> ~/OpenNMT/endeproj/endeproj_model/trans/BLEU_scores.txt;
#done
