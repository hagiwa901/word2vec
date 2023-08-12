import logging
import gensim
from gensim.models import Word2Vec

logging.basicConfig(level=logging.INFO)

def train(text_file:str, model_path: str) -> None:
    logging.info("train!!")
    with open(text_file) as f:
        sentences = [s.rstrip().split() for s in f.readlines()]
    logging.info(sentences)
    model = Word2Vec(sentences, min_count=1)
    logging.info(model_path)
    model.save(model_path)

def predict(model_path: str, word:str) -> None:
    model = Word2Vec.load(model_path)
    for item, value in model.wv.most_similar(word):
        print(item, value)