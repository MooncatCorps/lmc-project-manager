from mooncat.mcpm import metafile, paths
from pathlib import Path
import os, sys, shutil


# TODO: Implement correct logging
def install_library_files(name: str, lang: str, dev: bool = False) -> bool:
    path_from = paths.internal_library_files(lang)
    path_dest = paths.external_library_files(lang)

    if path_dest == None:
        sys.stderr.write(
f"""
Failed to install library files
Could not determine destination
This is usually caused by a misconfigured language name

[Relevant Settings]
development.lang = {lang}
"""
)

        return False

    if path_from == None:
        sys.stderr.write(
f"""
Failed to install library files
Could not determine source
This is usually caused by a misconfigured language name

[Relevant Settings]
development.lang = {lang}
"""
)

        return False

    path_dest = paths.append_mooncat(path_dest)

    if not paths.can_delete(path_dest):
        sys.stderr.write(
f"""
Failed to install library files
Cannot write to or clean destination ({path_dest})

[Permissions Required]
Write, Execute
"""
)
        return False

    if not paths.can_read(path_from):
        sys.stderr.write(
f"""
Failed to install library files
Cannot read from source ({path_dest})

[Permissions Required]
Read
"""
)
        return False

    path_dest /= name

    if path_dest.exists():
        paths.remove(path_dest)

    paths.copy(path_from, path_dest, symlink = dev)

    return True

    

