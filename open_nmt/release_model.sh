#!/usr/bin/env bash

# It will generate a en-de-model_epoch13_10.10_release.t7 file (Support cpu and gpu when translating, and take up less disk space)
# Note: if you training a model with GPU, you must use `-gpuid` when releasing
# Warning: released models can no longer be used for training
th $OPENNMT_HOME/tools/release_model.lua -model output/en-de-model_epoch13_10.10.t7
