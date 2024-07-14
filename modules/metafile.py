from witherlabs.projman import paths
from pathlib import Path
import tomllib


LAB_NAMESPACE = 'witherlabs'
METAFILE_NAME = '.wither'


def path() -> Path:
    return paths.cwd()/METAFILE_NAME



def exists() -> bool:
    path = paths.metafile()
    return path.exists()


def is_file() -> bool:
    path = paths.metafile()
    return path.is_file()


def is_valid() -> bool:
    return exists() and is_file()


def is_invalid() -> bool:
    return not is_valid()


def is_readable() -> bool:
    return paths.can_read(paths.metafile())


def create() -> bool:
    if is_valid():
        return True

    with open(paths.metafile(), 'x'):
        return True


def parse() -> dict:
    with open(paths.metafile(), 'rb') as metafile:
        return tomllib.load(metafile)

