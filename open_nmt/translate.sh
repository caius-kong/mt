#!/usr/bin/env bash

# Note1: if you training a model with GPU and model is not release, you must use `-gpuid` when translating
# -model 指定使用哪个epoch model进行翻译，src-test.txt是翻译测试文件，pred.txt是生成的翻译预测文件
# 翻译日志中：PRED PPL 是模型自身预测的困惑；GOLD PPL 根据您的模型，是黄金数据的困惑
th $OPENNMT_HOME/translate.lua -model output/en-de-model_epoch13_10.10_release.t7 -src input/en-de/src-test.txt -output output/en-de-pred13.txt
