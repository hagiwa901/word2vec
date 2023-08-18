import logging
import hydra
from omegaconf import DictConfig, OmegaConf
import gensim
from gensim.models import Word2Vec

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


@hydra.main(version_base=None, config_path="conf", config_name="config")
def main(cfg: DictConfig) -> None:
    logging.info("train start")
    text_file = cfg.config.text_file
    model_path = cfg.config.model_path
    logging.info("read_text ")
    with open(text_file) as f:
        sentences = [s.rstrip().split() for s in f.readlines()]
    logging.info("read_text done")
    min_count = cfg.word2vec.min_count
    model = Word2Vec(sentences, min_count=min_count)
    logging.info("word2vec model path:" + model_path)
    model.save(model_path)
    logging.info("train done")


if __name__ == '__main__':
    main()
