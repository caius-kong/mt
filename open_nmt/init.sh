#!/usr/bin/env bash

# just for nvidia-docker (ps、source init.sh)
export OPENNMT_HOME=/root/opennmt
export LUA_PATH="$LUA_PATH;$OPENNMT_HOME/?.lua"
