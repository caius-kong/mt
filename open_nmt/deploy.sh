#!/usr/bin/env bash

######################################################
# Note: http://zh.opennmt.net/OpenNMT/tools/servers/ #
######################################################

# Please use export THC_CACHING_ALLOCATOR=0 to save memory on server side.
#export THC_CACHING_ALLOCATOR=0

# need restserver-xavante package
#luarocks install restserver-xavante

# 1、Single Model Rest server (first version, kept for backward compatiblity)
# optional: -host 127.0.0.1 (如果您想要支持远程访问，请改用 0.0.0.0)
# optional: -port 7784
# optional: using any of the arguments from tokenize.lua or translate.lua (注意：必须附加标记化时的参数，否则访问时500 Internal Server Error)
th $OPENNMT_HOME/tools/rest_translation_server.lua -model output/en-de-model_epoch5_20.44.t7 -host 0.0.0.0 -port 7784 -mode aggressive -case_feature true -joiner_annotate true &

# test
#curl -v -H "Content-Type: application/json" -X POST -d '[{ "src" : "Hello World" }]' http://127.0.0.1:7784/translator/translate

# 2、Multi Model Rest server
#luarocks install yaml
#th $OPENNMT_HOME/tools/rest_multi_models.lua -gpuid 1 -model_config rest_config.yml -log_file /var/tmp/deploy.log &

# 3、Use ZeroMQ
#sudo apt-get install libzmq-dev   ==> http://zeromq.org/docs:source-git
#luarocks install dkjson
#luarocks install lua-zmq ZEROMQ_LIBDIR=/usr/lib/x86_64-linux-gnu/ ZEROMQ_INCDIR=/usr/include
#
#th tools/translation_server.lua -host ... -port ... -model ...
