# word2vec
## 概要
word2vecの前処理 ~ 予測までのコード

## 環境
- Mac

- python：3.8.9
  - gensim：4.3.1

- Docker：20.10.0

- docker-compose：1.27.4

# 実行方法
## 前処理
### データセット
https://qiita.com/kenta1984/items/93b64768494f971edf86
上の記事を参考に日本語のWikipediaをダウンロードする。

1. [こちら](https://dumps.wikimedia.org/jawiki/latest/)から[jawiki-latest-pages-articles.xml.bz2](https://dumps.wikimedia.org/jawiki/latest/jawiki-latest-pages-articles.xml.bz2)をダウンロード  
```
rye run download-wiki
```
2. [こちらのページ](https://github.com/attardi/wikiextractor)を参考にwikipediaの記事を取得
```
rye run wiki-extract
```
3. wikipediaの記事をテキストファイルに保存
```
rye run make-wiki-corpus
```
### 分かち書き
形態素解析器はMeCab+IPA辞書  
#### 実行
```
docker-compose build mecab_ipadic_tokenizer
docker-compose run mecab_ipadic_tokenizer
```
#### 実行結果
デフォルトの設定では`dataset/wiki.txt`を1行ごとに1文を記述。

wiki.txt
```
すもももももももものうち
今日もしないとね。
MeCabは便利です。
```

デフォルトの設定では`dataset/`直下に`wakati.txt`を作成して、1行ごとに単語分割された1文を出力。

wakati.txt
```
すもも も もも も もも の うち 
今日 も し ない と ね 。 
MeCab は 便利 です 。 
```

テキストファイル名を変更したい場合は`.env`を編集。  
分かち書きしたいテキストファイル名を`INPUT_TEXT`に代入。  
分かち書きした後のファイル名の出力結果を`OUTPUT_TEXT`に代入。  
#### 後処理
```
docker-compose down -v
```

## 学習
```
rye run train-script
```

## 予測
```
rye run predict-script
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