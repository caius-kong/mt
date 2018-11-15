#!/usr/bin/env bash

th $OPENNMT_HOME/translate.lua -model output/en-de-model_epoch5_20.44.t7 -src input/en-src-test.txt -output output/pred-5.txt