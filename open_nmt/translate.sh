#!/usr/bin/env bash

th $OPENNMT_HOME/translate.lua -model output/en-de-model_epoch13_9.07.t7 -src input/en-src-test.txt -output output/pred13.txt