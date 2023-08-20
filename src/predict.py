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
    logging.info("predict start")
    logging.info(OmegaConf.to_yaml(cfg))
    model_path = cfg.config.model_path
    word = cfg.predict.similar.word
    topn = cfg.predict.similar.topn
    model = Word2Vec.load(model_path)
    for item, value in model.wv.most_similar(word, topn=topn):
        print(item, value)
    logging.info("predict done")


if __name__ == '__main__':
    main()
