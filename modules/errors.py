import logging

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
