"""
PythonDocxAJM.py

My python-docx class

"""

from _version import __version__
from EasyLoggerAJM import EasyLogger
import docx
from pathlib import Path
from DocConfig import DocConfig
from __init__ import __project_name__

class _TemplateLockedError(Exception):
    """
    This class is an exception and inherits from the base `Exception` class.

    Attributes:
        None

    Methods:
        None

    Exceptions:
        None

    Note:
        This class is intended to be used as a custom exception when a template is locked and any modifications to it are attempted.

    Example:
        None

    """
    ...


class PythonDocxAJM:
    """
    Class representing a Python library for working with docx files.

    This class provides functionality to create and save docx files using docx templates.

    Attributes:
        _logger (Logger): The logger object to use for logging.
        _config (DocConfig): The configuration object to use for retrieving configuration values.
        file_save_path (str): The path where the docx file will be saved.
        file_template_path (str): The path to the docx template file.

    Methods:
        __init__ (self, **kwargs): Initializes a new instance of the PythonDocxAJM class.

            Args:
                **kwargs: Additional keyword arguments.
                    logger (Logger): The logger object to use. If not provided, a default logger will be used.
                    config (DocConfig): The configuration object to use. If not provided, a default configuration will be used.
                    config_list_dict (dict): A dictionary containing configuration values. If provided, it will override the values retrieved from the configuration object.

        save (self, path_to_file=None, **kwargs): Saves the docx file to the specified location.

            Args:
                path_to_file (str): The path where the docx file will be saved. If not provided, the value of file_save_path will be used.
                **kwargs: Additional keyword arguments.
                    create_dir (bool): Whether to create the directory if it does not exist. Defaults to False.

            Returns:
                str: The path to the saved docx file.
    """
    def __init__(self, **kwargs):
        # TODO: customize logger
        self._logger = kwargs.get('logger', EasyLogger(root_log_location='../logs',
                                                       project_name=__project_name__))
        self._config = kwargs.get('config', DocConfig(config_dir='../cfg', config_filename='config.ini',
                                                      logger=self._logger.logger,
                                                      config_list_dict=kwargs.get('config_list_dict', None)))
        self._config.GetConfig()

        self.file_save_path = self._config.get('DEFAULT', 'file_save_path')
        self.file_template_path = self._config.get('DEFAULT', 'file_template_path')
        if self.file_template_path:
            self.Document = docx.Document(self.file_template_path)
        else:
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
