from BetterConfigAJM import BetterConfigAJM as BetterConfig
from typing import List


class DocConfig(BetterConfig):
    DEFAULT_FILE_SAVE_PATH: str = None
    DEFAULT_LIST_DICT: List[dict] = None
    def __init__(self, *args, **kwargs):
        self.config_list_dict: List[dict] = None