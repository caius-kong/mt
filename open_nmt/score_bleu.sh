#!/usr/bin/env bash

# REFERENCE is either a single file, or a prefix for multiple-reference REFERENCE0, REFERENCE1, ... （参考文件）
# OUT （系统翻译输出,预测文件）
# 参考文件和系统输出必须是句子对齐的（参考文件中的行X对应于系统输出中的行X）。
# 如果存在多个引用转换，则必须将它们存储在单独的文件中并命名为reference0，reference1，reference2等。
# 所有文本都需要进行标记化。

# Optional: -sample 1       (If > 1, number of samples for estimation of k-fold error margin (95% certitude) - 10 is a good value.)
# Optional: -scorer bleu    (Accept: bleu|ter|dlratio)
# Optional: -order 4        (Number of sample for estimation of error margin)
th $OPENNMT_HOME/tools/score.lua input/en-de/tgt-test.txt < output/en-de-pred13.txt