# word2vec
## 概要
word2vecの事前学習 ~ テストまでのコード

## 環境
- python：3.8.9
  - gensim：4.3.1

- Docker：20.10.0

# 実行方法
## 前処理
```
docker-compose build mecab_ipadic_tokenizer
docker-compose up mecab_ipadic_tokenizer
```

## 学習
```
rye run train-script
```

# モジュール
## インストール
```
rye add [モジュール名]
```

## ロックファイルの作成
```
rye sync
```
