from typing import Any
from mooncat.mcpm import metafile, metadata
from mooncat.mcpm import installers
import logging

class LogFormatter(logging.Formatter):

    grey = "\x1b[38;20m"
    magenta = "\x1b[35;20m"
    yellow = "\x1b[33;20m"
    red = "\x1b[31;20m"
    bold_red = "\x1b[31;1m"
    reset = "\x1b[0m"
    fmt = "[%(levelname)s] (%(name)s) %(message)s"

    FORMATS = {
        logging.DEBUG: grey + fmt + reset,
        logging.INFO: magenta + fmt + reset,
        logging.WARNING: yellow + fmt + reset,
        logging.ERROR: red + fmt + reset,
        logging.CRITICAL: bold_red + fmt + reset
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)


logger = logging.getLogger("MCPM")
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
handler.setLevel(logging.DEBUG)
handler.setFormatter(LogFormatter())
logger.addHandler(handler)


def _get_metadata_or_quit() -> dict:
    data = metafile.interactive_parse(logger)
    if data == None:
        logger.critical("Could not determine project metadata")
        quit(1)

    return data


def _get_property_or_quit(key: str, data: dict) -> Any:
    val = metadata.get(key, data)
    if val == None:
        logger.critical("Could not determine project property: {key}")
        quit(1)

    return val


def install(isdev: bool = False):
    logger.debug("Fetching metadata...")
    data = _get_metadata_or_quit()

    p_name: str = _get_property_or_quit("project.name", data)
    p_type: str = _get_property_or_quit("project.type", data)
    p_lang: str = _get_property_or_quit("development.lang", data)

    logger.debug(f"Name: {p_name}")
    logger.debug(f"Type: {p_type}")
    logger.debug(f"Lang: {p_lang}")

    for typebit in p_type.split("+"):
        typebit = typebit.strip()

        if typebit == "library":
            installers.install_library_files(p_name, p_lang, logger, dev = isdev)


