#!/usr/bin/env bash

# continue the training from the last checkpoint. (If you not use '-continue', it's means training incrementally. Note: replace en-de-train.t7)
th $OPENNMT_HOME/train.lua -data output/en-de-train.t7 -save_model output/en-de-model -train_from output/en-de-model_epoch3_36.14.t7 -continue