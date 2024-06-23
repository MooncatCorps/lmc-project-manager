import logging
from pathlib import Path

def tripartite_error(what: str, why: str, cause: str, logger: logging.Logger):
    logger.error(what)
    logger.error(why)
    logger.info(cause)

def settings_issue(keys: list[str], reason: str, logger: logging.Logger):
    logger.error(f"{reason}: {', '.join(keys)}")

def missing_settings(keys: list[str], logger: logging.Logger):
    settings_issue(keys, "Missing settings", logger)

def misconfigured_settings(keys: list[str], logger: logging.Logger):
    settings_issue(keys, "Misconfigured settings", logger)

def file_permissions(keys: list[str], logger: logging.Logger):
    settings_issue(keys, "Missing File Permissions", logger)

def file_not_found(path: Path, logger: logging.Logger):
    logger.error("File not found")
    logger.error(f"Could not locate {path}")
    logger.info("Check for filesystem permissionsor missing files")

def insufficient_file_permissions(path: Path, keys: list[str], logger: logging.Logger):
    logger.error("Insufficient File Permissions")
    logger.error(f"Cannot operate on path {path}")
    logger.error("Check your filesystem permissions")
    file_permissions(keys, logger)

def misconfiguration(what_it_caused: str, settings_with_their_whys: dict[str, str], logger: logging.Logger):
    logger.error("Misconfiguration")
    logger.error("An error ocurred due to misconfigured settings in .mooncat.toml")
    logger.error(what_it_caused)

    logger.info("Problematic settings and why they matter:")
    for setting, reason in settings_with_their_whys:
        logger.info(f"Problem: {setting} -> {reason}")
