import logging
import re
from tqdm import tqdm
import hydra
from omegaconf import DictConfig, OmegaConf
import os

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


@hydra.main(version_base=None, config_path="conf", config_name="config")
def main(cfg: DictConfig) -> None:
    dir_root_path = cfg.config.dir_root_path
    save_text = cfg.config.save_text
    wiki_dir_list = os.listdir(dir_root_path)
    wiki_text = ''
    pattern = re.compile(r'[^</*doc.*]|[^\S]')
    for dir_list in tqdm(wiki_dir_list):
        wiki_dir_path = os.path.join(dir_root_path, dir_list)
        wiki_file_list = os.listdir(wiki_dir_path)
        for wiki_file in tqdm(wiki_file_list, leave=False):
            wiki_file_path = os.path.join(wiki_dir_path, wiki_file)
            with open(wiki_file_path) as f:
                sentences = [s.rstrip() for s in f.readlines()]
                for sentence in sentences:
                    if pattern.match(sentence):
                        wiki_text += sentence + '\n'
    with open(save_text, 'w') as f:
        f.write(wiki_text)


if __name__ == '__main__':
    main()
