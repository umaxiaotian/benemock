#!/bin/bash

if ! docker-compose ps --services | grep -q ansible; then
    echo "ansibleコンテナが動作していません。先にansibleコンテナを起動してください。"
    exit 1
fi

echo "" > Ansible/ssh/known_hosts

# コンテナ内で実行するコマンド
COMMAND="ssh-keyscan target-node-1 >> /root/.ssh/known_hosts"

# Dockerコマンドを実行
docker exec -it ansible sh -c "$COMMAND"