#!/usr/bin/env bash

# 训练平行语料，包含会议、新闻、网络爬取
wget https://s3.amazonaws.com/opennmt-trainingdata/wmt15-de-en.tgz
tar xzf wmt15-de-en.tgz
# 测试平行语料
wget http://www.statmt.org/wmt15/dev-v2.tgz
tar xzf dev-v2.tgz
cp dev/newstest2012.en dev/newstest2012.de wmt15-de-en

# 标记化、合并、复制（以文件实际路径为准）
#cd ~/OpenNMT/
#for f in ../wmt15-de-en/* ; do th tools/tokenize.lua -mode aggressive -case_feature true -joiner_annotate true < $f > $f.tok ; done
#for l in en de ; do cat ../wmt15-de-en/commoncrawl.de-en.$l.tok ../wmt15-de-en/europarl-v7.de-en.$l.tok ../wmt15-de-en/news-commentary-v10.de-en.$l.tok > ../wmt15-de-en/wmt15-all-de-en.$l.tok ; done
#cp ../wmt15-de-en/wmt15-all-de-en.*.tok ../wmt15-de-en/newstest*.tok ~/mt/open_nmt/input/en-de-general-wmt15/






