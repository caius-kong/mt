#!/usr/bin/env bash

# just for nvidia-docker (ps、直接执行，SHELL脚本中的export无法生效, 需要source init.sh)
export OPENNMT_HOME=/root/opennmt
export LUA_PATH="$LUA_PATH;$OPENNMT_HOME/?.lua"
