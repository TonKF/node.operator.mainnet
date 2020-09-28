#!/bin/bash

sudo apt update -y
sudo apt upgrade -y

#install dependencies
sudo apt install bc -y

#set env
cd ${NODE_OPERATOR_SCRIPTS_DIR} && . ${NODE_OPERATOR_CONFIGS_DIR}/env.sh

#install node
cd && git clone https://github.com/tonlabs/net.ton.dev.git
mv ~/net.ton.dev ~/main.ton.dev

cd ${SCRIPTS_DIR}
. ./env.sh
./build.sh
export NETWORK_TYPE=net.ton.dev
./setup.sh
./run.sh
