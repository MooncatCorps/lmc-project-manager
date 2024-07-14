import os, platform, sysconfig, shutil
from pathlib import Path
from typing import Optional


LAB_NAMESPACE = 'witherlabs'
METAFILE_NAME = '.wither'


#
# OS
#


def cwd() -> Path:
    return Path(os.getcwd())


def can_read(path: Path):
    return path.exists() and os.access(path, os.R_OK)


def can_write(path: Path):
    return path.exists() and os.access(path, os.W_OK)


def can_delete(path: Path):
    return path.exists() and os.access(path, os.W_OK | os.X_OK)


def has_access(path: Path):
    return path.exists() and os.access(path, os.W_OK | os.X_OK | os.R_OK)


def get_file_entity_name(path: Path):
    if path.is_dir():
        return 'directory'

    if path.is_file():
        return 'file'

    if path.is_mount():
        return 'mountpoint'

    if path.is_symlink():
        return 'symlink'

    if path.is_block_device():
        return 'block device'

    if path.is_char_device():
        return 'char device'

    if path.is_fifo():
        return 'fifo'

    if path.is_socket():
        return 'socket'


def remove(path: Path):
    if not path.is_dir() or path.is_symlink():
        os.remove(path)
    else:
        shutil.rmtree(path)


def copy(path_from: Path, path_dest: Path, symlink: bool = False):
    if symlink:
        os.symlink(path_from, path_dest)
    else:
        if path_from.is_dir():
            shutil.copytree(path_from, path_dest)
        else:
            shutil.copy(path_from, path_dest)


#
# Standard Files
#


def metafile() -> Path:
    return cwd()/METAFILE_NAME


#
# Language Specific: External Paths
#


def internal_library_files(lang: str) -> Optional[Path]:
    match lang:
        case 'python':
            return cwd()/'modules'
        case 'c' | 'c++':
            return cwd()/'include'

    return None


#
# Constants
#


def append_namespace(path: Path) -> Path:
    return path/LAB_NAMESPACE


