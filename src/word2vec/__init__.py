import logging
import gensim
from gensim.models import Word2Vec

logging.basicConfig(level=logging.INFO)

def hello() -> None:
    return "Hello from word2vec!"

def train(text_file:str, model_path: str) -> None:
    logging.debug("train!!")
    with open(text_file) as f:
        sentences = [s.rstrip().split() for s in f.readlines()]
    logging.debug(sentences)
    model = Word2Vec(sentences,min_count=1)
    logging.debug(model_path)
    model.save(model_path)
