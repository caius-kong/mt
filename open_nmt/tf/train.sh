#!/usr/bin/env bash

# OpenNMT-tf使用唯一的入口点：onmt-main。
# onmt-main <run_type> --model_type <model> --auto_config --config <config_file.yml>
#
# 3个基本元素:
# run_type                   (train_and_eval，train，eval，infer，export，score)
# -- model_type NMTSmall     (http://opennmt.net/OpenNMT-tf/package/opennmt.models.catalog.html)
# --auto_config              (Automatically selects the best settings for this type of model)

onmt-main train_and_eval --model_type NMTSmall --auto_config --config data.yml