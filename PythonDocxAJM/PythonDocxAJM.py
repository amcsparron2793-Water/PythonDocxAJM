"""
PythonDocxAJM.py

My python-docx class

"""

from _version import __version__
import datetime
from BetterConfigAJM import BetterConfigAJM as BetterConfig
from EasyLoggerAJM import EasyLogger
import docx
from pathlib import Path


class _TemplateLockedError(Exception):
    ...


class PythonDocxAJM:
    def __init__(self, **kwargs):
        # TODO: customize logger and config to fit needs
        self._logger = kwargs.get('logger', EasyLogger(root_log_location='../logs'))
        self._config = kwargs.get('config', BetterConfig(config_dir='../cfg', config_filename='config.ini',
                                                         config_list_dict=kwargs.get('config_list_dict',
                                                                                     [{'DEFAULT': {'test': 'testvalue'}}])))
        self._config.GetConfig()

        # TODO: get these into a config file/read from that file
        self.file_save_path = None
        self.file_template_path = None
        self.Document = docx.Document()


def save(self, path_to_file=None, **kwargs):
    create_dir = kwargs.get('create_dir', False)

    if path_to_file is None:
        path_to_file = self.file_save_path
        file_parent_dir = Path(path_to_file).parent
    else:
        file_parent_dir = Path(path_to_file).parent
        if file_parent_dir.is_dir():
            self._logger.debug(f'Save location {file_parent_dir} detected')
        else:
            if not create_dir:
                try:
                    raise NotADirectoryError(f"Folder chosen as save location"
                                             f" ({Path(path_to_file).parent}) does not exist.")
                except NotADirectoryError as e:
                    self._logger.error(e, exc_info=True)
                    raise e
            else:
                self._logger.debug(f'Save location {file_parent_dir} being created...')
                file_parent_dir.mkdir(exist_ok=True)

    if path_to_file == self.file_template_path:
        try:
            raise _TemplateLockedError('Cannot save over the template, please choose a different filename.')
        except _TemplateLockedError as e:
            self._logger.error(e, exc_info=True)
            raise e

    self.Document.save(path_to_file)
    self._logger.info(f'Saved file to {file_parent_dir.resolve()}')
    return Path(path_to_file).resolve()


if __name__ == '__main__':
    PythonDocxAJM()
