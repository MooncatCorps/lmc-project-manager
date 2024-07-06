import re
import tomllib
import logging
from typing import Optional
from witherlabs.projman import paths


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


def interactive_create(logger: logging.Logger) -> bool:

    if not exists():
        logger.warn(f'Missing {paths.METAFILE_NAME}')

        if not input('Create it now? [Y/n]').lower() in [ '', 'y', 'yes' ]:
            return False

        if not paths.can_write(paths.cwd()):
            logger.error(f'Insufficient permissions to create {paths.metafile()}')
            return False

        create()

    if is_invalid():
        logger.error(f'{paths.METAFILE_NAME} exists, but is not a regular file.')
        logger.info(f'{paths.METAFILE_NAME} is a {paths.get_file_entity_name(paths.metafile())}')
        return False
        

    return True


def interactive_parse(logger: logging.Logger) -> Optional[dict]:

    val = None

    if not interactive_create(logger):
        return val

    content = ''

    with open(paths.metafile(), 'r') as metafile:
        content = metafile.read()

    try:
        val = tomllib.loads(content)
    except tomllib.TOMLDecodeError as err:
        reason = str(err)
        logger.error(f'The {paths.METAFILE_NAME} file contains errors')
        logger.error(f'Reason: {reason}')

        match = re.search(r'\(at line (.*), column (.*)\)', reason)

        if not match:
            return val

        str_line = match.groups()[0]
        str_column = match.groups()[1]

        if not str_line.isnumeric() or not str_column.isnumeric():
            return val

        line = int(str_line)
        column = int(str_column)

        lnstr = content.split('\n')[line - 1]
        logger.info(f'{paths.METAFILE_NAME}:\n{line}:\t{lnstr}\n{' ' * len(str_line)} \t{' ' * (column - 2)}^^^\n')


    return val










