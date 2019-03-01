import logging
import logging.config
import yaml
from pathlib import Path
from os import path

SRC_DIR = Path(__file__).resolve().parents[0]

with open(path.join(SRC_DIR, 'configs/config.yml')) as config_file:
    CONFIG = yaml.safe_load(config_file)
    logging.config.dictConfig(CONFIG)
