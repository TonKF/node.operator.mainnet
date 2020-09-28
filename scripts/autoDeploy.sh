#!/bin/bash

username=$(whoami)
hostname=$(hostname -s)

mv ~/validator.json ~/ton-keys/msig.keys.json
mv ~/validator.addr ~/ton-keys/$hostname.addr
mv ~/pubkey.json ~/ton-keys/pubkey.json

pubkey1=$(echo 0x$(cat ~/ton-keys/msig.keys.json | grep 'public' | awk '{print $2}' | tr -d '"'\,))
pubkey2=$(echo 0x$(cat ~/ton-keys/pubkey.json))

cd ~/main.ton.dev/tonos-cli/target/release
./tonos-cli deploy ~/main.ton.dev/configs/SafeMultisigWallet.tvc \
        "{"\"owners"\":["\"${pubkey1}"\","\"${pubkey2}"\"],"\"reqConfirms"\":2}" \
        --abi ~/main.ton.dev/configs/SafeMultisigWallet.abi.json \
        --sign ~/ton-keys/msig.keys.json \
        --wc -1     
