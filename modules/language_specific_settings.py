from witherlabs.projman import paths, metadata
from typing import Optional
from pathlib import Path

import sysconfig, platform


SUPPORTED_LANGUAGES = ['python', 'c', 'c++']


def _unix_system_library_directory_for(language_name: str) -> Path:
    """Returns a path to which libraries of the given language should be installed (for Unix systems)"""
    match language_name:
        case 'python':
            return Path(sysconfig.get_paths()['purelib'])
        case 'c' | 'c++':
            return Path('/usr/include')

    return Path('')


def _windows_system_library_directory_for(language_name: str) -> Path:
    """Returns a path to which libraries of the given language should be installed (for Windows systems)"""
    raise NotImplementedError('Windows support is pending.')


def system_library_directory_for(language_name: str) -> Path:
    """Returns a path to which libraries of the given language should be installed"""
    if platform.system == 'Windows':
        return _windows_system_library_directory_for(language_name)

    return _unix_system_library_directory_for(language_name)


# Currently, supports passing in `language_name` in case a language requires special handling
#   such as intermediate directories
def append_namespace_to_system_library_directory(language_name: str, system_path: Path) -> Path:
    """Appends the 'witherlabs' signature to the installation destination"""
    return system_path/metafile.LAB_NAMESPACE


class Language:

    def __init__(self, name: str):
        self.name = name
        self.system_library_directory = system_library_directory_for(name)
        self.wither_system_library_directory = append_namespace_to_system_library_directory(name, self.system_library_directory)


def err_invalid_language(lang_name: str):
    return errors.WLPMError(errors.WLPMErrorType.LANGUAGE, f'Language not supported: {lang_name}')


def get_language(data: dict) -> errors.PossibleError[Language]:
    lang = metadata.get(settings.LANGUAGE, data)
    val = errors.PossibleError(lang)

    if lang is None:
        val.add_error(settings.err_setting_not_pressent(settings.LANGUAGE))
        return val

    if lang not in SUPPORTED_LANGUAGES:
        val.add_error(err_invalid_language(lang))
        return val

    val.set_value(Language(lang))

    return val


