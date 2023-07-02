# benemock(デモ用アプリ）

## 使い方

基本的に上から順にコマンドを実行していけば起動できます。

### まずは、起動しよう

デフォルトのdocker-compose.ymlで既に、ターゲットノードと発射台のノードがセットされています。本コンテナはDockerfileから最初にビルドする必要があるため、下記のコマンドで、ビルドしてください。

※PythonなどをPython3.11にバージョンアップしたりする処理を入れているので、１０分ほどかかります。（良いVMとかホスト使ってたら秒で終わります。。。。)

```bash
docker-compose build
```

ビルドが正常に終了したら、下記のコマンドを入力して、docker-composeの設定通りにコンテナを起動します。 -dオプションを付けることで、ターミナルに入らないようにして、起動できます。

```bash
docker-compose up -d
```

### 初めてターゲットノードに接続する

現在記載されているdocker-compose.ymlには予めターゲットノードである、target-node-1に接続するように設定されています。

コンテナを作成する際は、ターゲットノードに初めて接続するため、下記のコマンドを作ってknown_hostsに登録する必要があります。

```bash
ssh-keyscan target-node-1 >> /root/.ssh/known_hosts
```

### Ansible発射台サーバーに接続し、Playbookを動かす

まず発射台であるansibleコンテナ内に入ってください。※devContainerの機能を使ってGUIから入ってもらってもいいです。その人は下記のコマンドはパスしてください。

```bash
docker exec -it ansible bash
```

コンテナ内に入ると、docker-compose.ymlに記載されている通りwork_dir: /appつまり、/appフォルダ内に自動的に入ります。

そのファイルの中のplaybooksというフォルダ内にメインで処理するプレイブックが格納されているますので、下記のコマンドで、Playbookを実行します。

```bash
ansible-playbook playbooks/deploy.yml
```

そうすると、デプロイが、target-node-1に対して行われるはずです。

あとは好きなように使ってください。
