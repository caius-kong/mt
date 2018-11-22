#!/usr/bin/env bash

# Note1: if you training a model with GPU, you must use `-gpuid` when translating
# Note2: you can use `tools/release_model.lua` to release model. A released model takes less space on disk and is compatible with both CPU and GPU translation.
th $OPENNMT_HOME/translate.lua -model output/en-de-model_epoch13_10.10.t7 -src input/en-de/src-test.txt -output output/en-de-pred13.txt