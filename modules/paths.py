import os, stat, platform, sysconfig
from pathlib import Path
from typing import Optional

#
# OS
#


def cwd() -> Path:
    return Path(os.getcwd())


def can_read(path: Path):
    return os.access(path, os.R_OK)


def can_write(path: Path):
    return os.access(path, os.W_OK)


def get_file_entity_name(path: Path):
    if path.is_dir():
        return "directory"

    if path.is_file():
        return "file"

    if path.is_mount():
        return "mountpoint"

    if path.is_symlink():
        return "symlink"

    if path.is_block_device():
        return "block device"

    if path.is_char_device():
        return "char device"

    if path.is_fifo():
        return "fifo"

    if path.is_socket():
        return "socket"


#
# Standard Files
#


def metafile() -> Path:
    return cwd()/".mooncat.toml"


#
# Language Specific: External Paths
#


def _external_library_files_unix(lang: str) -> Optional[Path]:
    match lang:
        case "python" | "py":
            return Path(sysconfig.get_paths()["purelib"])
        case "c" | "c++":
            return Path("/usr/include")

    return None


def _external_library_files_windows(lang: str) -> Optional[Path]:
    # Later...
    return None


def external_library_files(lang: str) -> Optional[Path]:
    if platform.system == "Windows":
        return _external_library_files_windows(lang)

    return _external_library_files_unix(lang)

