#!/usr/bin/env bash

######################################################
# Note: http://zh.opennmt.net/OpenNMT/tools/servers/ #
######################################################

# Please use export THC_CACHING_ALLOCATOR=0 to save memory on server side.
#export THC_CACHING_ALLOCATOR=0

# need restserver-xavante package
#luarocks install restserver-xavante

# 1、Single Model Rest server (first version, kept for backward compatiblity)
th $OPENNMT_HOME/tools/rest_translation_server.lua -model output/en-de-model_epoch5_20.44.t7 -gpuid 1 -host ... -port -case_feature -bpe_model ...

# test
#curl -v -H "Content-Type: application/json" -X POST -d '[{ "src" : "Hello World" }]' http://127.0.0.1:7784/translator/translate

# 2、Multi Model Rest server
#luarocks install yaml
#th $OPENNMT_HOME/tools/rest_multi_models.lua -gpuid 1 --mode_config rest_config.yml

# 3、Use ZeroMQ
#sudo apt-get install libzmq-dev   ==> http://zeromq.org/docs:source-git
#luarocks install dkjson
#luarocks install lua-zmq ZEROMQ_LIBDIR=/usr/lib/x86_64-linux-gnu/ ZEROMQ_INCDIR=/usr/include
#
#th tools/translation_server.lua -host ... -port ... -model ...