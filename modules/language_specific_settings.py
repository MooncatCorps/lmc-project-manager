from typing import Optional
from witherlabs.projman import paths, metadata
from pathlib import Path
import sysconfig, platform


CONTEMPLATED_LANGUAGES = ['python', 'c', 'c++']


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
    return system_path/paths.LAB_NAMESPACE


class Language:

    def __init__(self, name: str, data: dict):
        self.is_valid = name in CONTEMPLATED_LANGUAGES
        self.name = name

        if not self.is_valid:
            return

        self.system_library_directory = system_library_directory_for(name)
        self.wither_system_library_directory = append_namespace_to_system_library_directory(name, self.system_library_directory)


def get_language(data: dict) -> Optional[Language]:
    lang = metadata.get('development.lang', data)
    if lang is None: return None

    return Language(lang, data)


