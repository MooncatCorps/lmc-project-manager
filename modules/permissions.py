from pathlib import Path
import os


def can_read(path: Path) -> bool:
    return path.exists() and os.access(path, os.R_OK)


def can_write(path: Path) -> bool:
    return path.exists() and os.access(path, os.W_OK)


def can_execute(path: Path) -> bool:
    return path.exists() and os.access(path, os.X_OK)


def can_delete(path: Path):
    permholder: Path
    if path.is_dir():
        permholder = path
    else:
        permholder = path.parent

    return can_read(permholder) and can_write(permholder) and can_execute(permholder)


