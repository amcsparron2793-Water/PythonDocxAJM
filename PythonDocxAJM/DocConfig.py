from BetterConfigAJM import BetterConfigAJM as BetterConfig


class DocConfig(BetterConfig):
    """
    This module provides a class `DocConfig` that extends the `BetterConfig` class. It is used for handling configuration settings related to document files.

    `DocConfig` has the following attributes:
    - `DEFAULT_FILE_SAVE_PATH`: A static attribute that holds the default file save path for documents.
    - `DEFAULT_LIST_DICT`: A static attribute that holds a list of default configuration dictionary for documents.

    `DocConfig` has the following methods:
    - `__init__(*args, **kwargs)`: The constructor method that initializes an instance of `DocConfig`. It calls the constructor of the `BetterConfig` superclass and then handles the config list dictionary passed as a keyword argument.
    - `_handle_config_list_dict(**kwargs)`: A private method that handles the config list dictionary passed as keyword arguments. It checks if the dictionary is None and removes it from the keyword arguments if it is.

    Usage:
    ```
    config = DocConfig()
    ```
    """
    DEFAULT_FILE_SAVE_PATH = '../Misc_Project_Files/default_filename.docx'
    DEFAULT_LIST_DICT = [
        {
            'DEFAULT': {
                'file_save_path': DEFAULT_FILE_SAVE_PATH,
                'file_template_path': ''
            }
        }
    ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._handle_config_list_dict(** kwargs)
        self.config_list_dict = kwargs.get('config_list_dict', self.DEFAULT_LIST_DICT)

    def _handle_config_list_dict(self, ** kwargs):
        if 'config_list_dict' in kwargs and kwargs['config_list_dict'] is None:
            kwargs.__delitem__('config_list_dict')
            self._logger.debug('config_list_dict kwarg was none, item was deleted from kwargs.')