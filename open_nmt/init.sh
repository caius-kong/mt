#!/usr/bin/env bash

# just for nvidia-docker
export OPENNMT_HOME=/root/opennmt
export LUA_PATH="$LUA_PATH;$OPENNMT_HOME/?.lua"

# Make sure the container does not exit after executing the script
tail -f /dev/null