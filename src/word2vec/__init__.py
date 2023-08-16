import logging
import gensim
from gensim.models import Word2Vec


logging.getLogger(__name__).addHandler(logging.NullHandler())

def predict(model_path: str, word:str) -> None:
    model = Word2Vec.load(model_path)
    for item, value in model.wv.most_similar(word):
        print(item, value)