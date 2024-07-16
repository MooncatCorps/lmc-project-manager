import os, shutil
from pathlib import Path


def cwd() -> Path:
    return Path(os.getcwd())


def remove(path: Path):
    if not path.is_dir() or path.is_symlink():
        os.remove(path)
    else:
        shutil.rmtree(path)


def copy(path_from: Path, path_dest: Path):
    if path_from.is_dir():
        shutil.copytree(path_from, path_dest)
    else:
        shutil.copy(path_from, path_dest)


def symlink(path_from: Path, path_dest: Path):
    os.symlink(path_from, path_dest)


def can_read(path: Path) -> bool:
    return path.exists() and os.access(path, os.R_OK)


def can_write(path: Path) -> bool:
    return path.exists() and os.access(path, os.W_OK)


def can_execute(path: Path) -> bool:
    return path.exists() and os.access(path, os.X_OK)


def can_delete(path: Path) -> bool:
    permholder = path.parent
    return can_read(permholder) and can_write(permholder) and can_execute(permholder)


def get_file_entity_name(path: Path) -> str:
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

    return 'unknown'

