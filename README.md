# 環境構築手順

Qiitaの下記の記事を参考に「pip3のインストール」まで行う
https://gaiax.qiita.com/k_shibuya/items/c95754cf7f7a4c49c97b#pip3%E3%81%AE%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB

このアプリではパッケージをPipenvで管理しているので、その後は以下を参照

## Pipenvのインストール

```
$ pip3 install pipenv
```

## データベース作成

```
$ mysql -u root -p
$ create database ginstagram
```

## パッケージのインストール

```
$ pipenv install --dev
```

## DBのmigrate

```
$ pipenv run python manage.py migrate
```

# アプリ実行

```
$ pipenv run start
```

ブラウザで以下のURLにアクセス
http://127.0.0.1:8888

# テスト実行

```
$ pipenv run test
```
