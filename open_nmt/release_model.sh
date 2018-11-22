#!/usr/bin/env bash

# It will generate a en-de-model_epoch13_10.10_release.t7 file
# Warning: released models can no longer be used for training
th $OPENNMT_HOME/tools/release_model.lua -model output/en-de-model_epoch13_10.10.t7