import logging
import gensim
from gensim.models import Word2Vec

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def main(text_file: str, model_path: str) -> None:
    logging.info("train start")
    with open(text_file) as f:
        sentences = [s.rstrip().split() for s in f.readlines()]
    model = Word2Vec(sentences, min_count=1)
    logging.info("word2vec model path:" + model_path)
    model.save(model_path)
    logging.info("train done")


if __name__ == '__main__':
    main()
