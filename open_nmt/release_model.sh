#!/usr/bin/env bash

# It will generate a en-de-model_release.t7 file
# Warning: The script need `-gpuid` and released models can no longer be used for training
th $OPENNMT_HOME/tools/release_model.lua -model en-de-model_epoch13_10.10.t7 -gpuid 1