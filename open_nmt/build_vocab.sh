#!/usr/bin/env bash

# 预先生成词汇表，供预处理使用。（在对新数据重新训练模型时尤其需要：词汇必须相同）
th $OPENNMT_HOME/build_vocab.lua -data input/en-de/src-train.txt -save_vocab en-de
th $OPENNMT_HOME/build_vocab.lua -data input/en-de/tgt-train.txt -save_vocab en-de