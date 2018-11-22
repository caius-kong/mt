#!/usr/bin/env bash

th $OPENNMT_HOME/preprocess.lua -train_src input/en-de/src-train.txt -train_tgt input/en-de/tgt-train.txt -valid_src input/en-de/src-val.txt -valid_tgt input/en-de/tgt-val.txt -save_data output/en-de