import sys
import re
import tomllib
from mooncat.mcpm import paths


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

    with open(paths.metafile(), "x"):
        return True


def parse() -> dict:
    with open(paths.metafile(), "rb") as metafile:
        return tomllib.load(metafile)


def interactive_create() -> bool:
    if not exists():
        sys.stderr.write("Warning: Missing .mooncat.toml\n")

        if not input("Create it now? [Y/n]").lower() in [ "", "y", "yes" ]:
            return False

        if not paths.can_write(paths.cwd()):
            sys.stderr.write(f"Error: Insufficient permissions to create {paths.metafile()}\n")
            return False

        create()

    if is_invalid():
        sys.stderr.write("Error: .mooncat.toml exists, but is not a regular file.\n")
        sys.stderr.write(f"Hint: .mooncat.toml is a {paths.get_file_entity_name(paths.metafile())}\n")
        return False
        

    return True


def interactive_parse() -> dict:
    val = {}

    if not interactive_create():
        return val

    content = ""

    with open(paths.metafile(), "r") as metafile:
        content = metafile.read()

    try:
        val = tomllib.loads(content)
    except tomllib.TOMLDecodeError as err:
        reason = str(err)
        sys.stderr.write("Error: The .mooncat.toml file contains errors\n")
        sys.stderr.write(f"Reason: {reason}\n")

        match = re.search(r"\(at line (.*), column (.*)\)", reason)

        if not match:
            return val

        str_line = match.groups()[0]
        str_column = match.groups()[1]

        if not str_line.isnumeric() or not str_column.isnumeric():
            return val

        line = int(str_line)
        column = int(str_column)

        lnstr = content.split("\n")[line - 1]
        sys.stderr.write(f".mooncat.toml:\n{line}:\t{lnstr}\n{' ' * len(str_line)} \t{' ' * (column - 2)}^^^\n")


    return val










