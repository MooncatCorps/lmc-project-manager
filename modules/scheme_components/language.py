from witherlabs.projman import path_util, metadata_constants
from witherlabs.projman.error_handling import Maybe
from pathlib import Path

import sysconfig, platform


SUPPORTED_LANGUAGES = ['python', 'c', 'c++']


def _err_libdir_not_found(lang_name: str, platform_name: str) -> Maybe[Path]:
    return Maybe(None, f'Could not determine library directory path for {lang_name} (platform = {platform_name})')


def _unix_system_library_directory_for(language_name: str) -> Maybe[Path]:
    match language_name:
        case 'python':
            return Maybe(Path(sysconfig.get_paths()['purelib']))
        case 'c' | 'c++':
            return Maybe(Path('/usr/include'))

    return _err_libdir_not_found(language_name, 'unix')


def _windows_system_library_directory_for(language_name: str) -> Maybe[Path]:
    raise NotImplementedError('Windows support is pending.')
    # return _err_libdir_not_found(language_name, 'windows')


def system_library_directory_for(language_name: str) -> Maybe[Path]:
    if platform.system == 'Windows':
        return _windows_system_library_directory_for(language_name)

    return _unix_system_library_directory_for(language_name)


# Currently, supports passing in `language_name` in case a language requires special handling
#   such as intermediate directories
def append_namespace_to_system_library_directory(language_name: str, system_path: Path) -> Path:
    return system_path/metadata_constants.ORGANIZATION_NAME


class Language:

    def __init__(self, name: str):
        self.name = name
        self.system_library_directory = system_library_directory_for(name)
        self.wither_system_library_directory = append_namespace_to_system_library_directory(name, self.system_library_directory)


def err_invalid_language(language_name: str) -> Maybe[Language]:
    return Maybe(None, f'Language not supported: {language_name}')


def get_langauge(language_name: str) -> Maybe[Language]:
    if language_name not in SUPPORTED_LANGUAGES:
        return err_invalid_language(language_name)

    return Maybe(Language(language_name))


