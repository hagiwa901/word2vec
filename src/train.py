import logging
from tqdm import tqdm
import hydra
from omegaconf import DictConfig, OmegaConf
import gensim
from gensim.models import Word2Vec

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


@hydra.main(version_base=None, config_path="conf", config_name="config")
def main(cfg: DictConfig) -> None:
    logging.info("train start")
    logging.info(OmegaConf.to_yaml(cfg))
    text_file = cfg.config.text_file
    model_path = cfg.config.model_path
    min_count = cfg.model.word2vec.min_count
    vector_size = cfg.model.word2vec.vector_size
    window = cfg.model.word2vec.window
    workers = cfg.model.word2vec.workers
    logging.info("read_text ")
    with open(text_file, encoding="UTF-8", errors='ignore') as f:
        sentences = [s.rstrip().split() for s in tqdm(f.readlines())]
    logging.info("read_text done")
    model = Word2Vec(sentences,
                     vector_size=vector_size,
                     min_count=min_count,
                     window=window,
                     workers=workers)
    logging.info("word2vec model path:" + model_path)
    model.save(model_path)
    logging.info("train done")


if __name__ == '__main__':
    main()
