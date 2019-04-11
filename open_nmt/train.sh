#!/usr/bin/env bash

# optional: -gpuid 0                                (List of GPU identifiers (1-indexed). CPU is used when set to 0)
# optional: -preprocess_pthreads 4                  (Number of parallel threads for preprocessing)
# optional: -log_file ''                            (Output logs to a file under this path instead of stdout)
# optional: -log_level INFO                         (accepted: DEBUG, INFO, WARNING, ERROR, NONE)
# optional: -validation_metric perplexity           (Metric to use for validation. Accepted: perplexity, loss, bleu, ter, dlratio)  (除此之外，还可以单独使用tools/score.lua)
# optional: -save_validation_translation_every 0    (When using validation metrics (e.g. BLEU, TER, etc.), also save the translation every this many epochs to the file _epochN_validation_translation.txt. If = 0, will not save validation translation.)
# optional: -end_epoch 13                           (If = 0, train forever unless -min_learning_rate is reached)
# optional: -optim sgd                              (accepted: sgd, adagrad, adadelta, adam) (训练优化方法。通常来说，sgd效率是最差的，adam效率是最好的，能迅速收敛。注意：数据量小时，适合sgd，慢但准)
# optional: -learning_rate 1                        (Recommended settings are: sgd = 1, adagrad = 0.1, adam = 0.0002.)
th $OPENNMT_HOME/train.lua -data output/en-de-train.t7 -save_model output/en-de-model -gpuid 1 -optim adam -learning_rate 0.0002
