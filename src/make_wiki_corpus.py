import logging
import os

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def main(dir_root_path: str, save_text: str) -> None:
    logging.info("make corpus")
    wiki_dir_list = os.listdir(dir_root_path)
    wiki_text = ''
    for dir_list in wiki_dir_list:
        wiki_dir_path = os.path.join(dir_root_path, dir_list)
        wiki_file_list = os.listdir(wiki_dir_path)
        for wiki_file in wiki_file_list:
            wiki_file_path = os.path.join(wiki_dir_path, wiki_file)
            with open(wiki_file_path) as f:
                sentences = [s.rstrip() for s in f.readlines()]
            for sentence in sentences:
                wiki_text += sentence + '\n'
            logging.info(wiki_file_path + " done")
    logging.info("save_text_file_name: " + save_text)
    with open(save_text, 'w') as f:
        f.write(wiki_text)
    logging.info("make corpus done")


if __name__ == '__main__':
    main()
