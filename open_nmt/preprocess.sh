#!/usr/bin/env bash

# 通常使用-src_vocab和-tgt_vocab选项跨数据集重用词汇表。在对新数据重新训练模型时尤其需要：词汇必须相同。
# Tip：可以使用tools/build_vocab.lua脚本预先生成词汇表
th $OPENNMT_HOME/preprocess.lua -train_src input/en-de/src-train.txt -train_tgt input/en-de/tgt-train.txt -valid_src input/en-de/src-val.txt -valid_tgt input/en-de/tgt-val.txt -save_data output/en-de
