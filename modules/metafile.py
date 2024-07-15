from witherlabs.projman import paths, permissions
from pathlib import Path
import tomllib


LAB_NAMESPACE = 'witherlabs'
METAFILE_NAME = '.wither'


def path() -> Path:
    return paths.cwd()/METAFILE_NAME



def exists() -> bool:
    return path().exists()


def is_file() -> bool:
    return path().is_file()


def is_valid() -> bool:
    return exists() and is_file()


def is_invalid() -> bool:
    return not is_valid()


def create() -> bool:
    if is_valid():
        return True

    with open(path(), 'x'):
        return True


def parse() -> dict:
    with open(path(), 'rb') as metafile:
        return tomllib.load(metafile)

