#!/usr/bin/env bash

th $OPENNMT_HOME/preprocess.lua -train_src input/en-src-train.txt -train_tgt input/de-tgt-train.txt -valid_src input/en-src-val.txt -valid_tgt input/de-tgt-val.txt -save_data output/en-de