import docx
from pathlib import Path
from logging import Logger
from EasyLoggerAJM import EasyLogger
from BetterConfigAJM import BetterConfigAJM as BetterConfig
from configparser import ConfigParser

class _TemplateLockedError(Exception):
    ...

class PythonDocxAJM:
    def __init__(self):
        self._logger:EasyLogger or Logger = None
        self._config: BetterConfig or ConfigParser = None

        self.file_save_path: Path or None = None
        self.file_template_path: Path or None = None
        self.Document:docx.Document = None

    def save(self, path_to_file:Path or str or None = None, **kwargs):
        ...