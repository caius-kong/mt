#!/usr/bin/env bash
# continue the training from the last checkpoint.
# case1: 恢复停止的训练：use '-continue', 确保训练继续具有相同的配置和优化状态
# case2: 使用基础模型并使用新的培训选项进一步训练它：not use '-continue' and add new options (-optim/-learning_rate)
# case3: 培训新数据模型（增量适应）：use '-update_vocab'，更改检查点中包含的单词词汇表（例如，添加域术语）。这对微调现有模型很有用。例如，在机器翻译中，与从头开始训练相比，将通用模型适应特定域更快。

# Note: 如果你单独使用-train_from，那么你将从模型的权重，嵌入和词汇等方面开始"新"的训练(1-end)；如果你同时还使用了-continue，即使你正在使用新数据，你仍是在继续进行培训（x-end）

# Optional: optim sgd           (accept: sgd, adagrad, adadelta, adam)
# Optional: -learning_rate 1    (Recommended settings are: sgd = 1, adagrad = 0.1, adam = 0.0002)
# Optional: -update_vocab none  (accept: none, replace, merge)
# replace: 仅保留常用词（删除非常用单词和旧的单词），初始化新的单词 (如果你想训练一个高度专业化的模型"replace"将是更好的选择)
# merge: 保留所有旧的单词，初始化新的单词

# case 1 example:
th $OPENNMT_HOME/train.lua -data output/en-de-train.t7 -save_model output/en-de-model -train_from output/en-de-model_epoch7_12.32.t7 -continue


# case3 example:
# 1、使用原词汇表预处理数据
# th $OPENNMT_HOME/preprocess.lua
#   -train_src input/en-de-new/src-train.txt
#   -train_tgt input/en-de-new/tgt-train.txt
#   -save_data output/en-de-new
# 2、增量训练
# th $OPENNMT_HOME/train.lua
#   -data output/en-de-new-train.t7
#   -save_model output/en-de-model
#   -train_from output/en-de-model_epoch13_12.32.t7
#   -update_vocab replace
#   -gpuid 1

# 参考：http://forum.opennmt.net/t/problem-with-incremental-in-domain-training/330/20