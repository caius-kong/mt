#!/usr/bin/env bash

th $OPENNMT_HOME/translate.lua -model output/en-de-model_epoch13_10.10.t7 -src input/en-de/src-test.txt -output output/en-de-pred13.txt