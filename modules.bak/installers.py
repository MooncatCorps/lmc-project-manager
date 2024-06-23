from mooncat.mcpm import paths, errors
import os
import logging


def install_library_files(name: str, lang: str, logger: logging.Logger, dev: bool = False) -> bool:
    logger.debug("Performing library installation")

    path_from = paths.internal_library_files(lang)
    path_base = paths.external_library_files(lang)

    logger.debug(f"Source Path: {path_from}")
    logger.debug(f"Base Destination Path: {path_base}")

    if path_base == None:
        errors.tripartite_error(
            "Failed to install library files",
            "Could not determine destination (to which files should be installed)",
            "This is usually caused by a misconfigured language name",
            logger)

        errors.misconfigured_settings(["development.lang"], logger)

        return False

    if not paths.can_delete(path_base):
        errors.tripartite_error(
            "Failed to install library files",
            f"Cannot operate on destination: {path_base}",
            "Do you have the right file permissions?",
            logger)

        errors.file_permissions(["write", "execute"], logger)
        return False

    if path_from == None:
        errors.tripartite_error(
            "Failed to install library files",
            "Could not determine source (from which to install files)",
            "This is usually caused by a misconfigured language name",
            logger)

        errors.misconfigured_settings(["development.lang"], logger)
        return False

    if not paths.can_read(path_from):
        errors.tripartite_error(
            "Failed to install library files",
            f"Cannot read from source: {path_from}",
            "Do you have the right permissions?",
            logger)

        errors.file_permissions(["read"], logger)
        return False

    path_moon = paths.append_mooncat(path_base)
    path_lib = path_moon/name

    logger.debug(f"Mooncat Destination Path: {path_moon}")
    logger.debug(f"Library Destination Path: {path_lib}")

    logger.debug(f"Attempting to create path: {path_moon}")
    os.makedirs(path_moon, exist_ok = True)

    if path_lib.exists():
        logger.debug(f"Cleaning up: {path_base}")
        paths.remove(path_lib)

    logger.debug(f"Copying {path_from} to {path_base}; Symlink = {dev}")
    paths.copy(path_from, path_lib, symlink = dev)

    logger.debug(f"Done")
    return True


def uninstall_library_files(name: str, lang: str, logger: logging.Logger) -> bool:
    path_dest = paths.external_library_files(lang)

    if path_dest == None:
        errors.tripartite_error(
            "Failed to uninstall library files",
            "Could not determine target (from which files should be removed)",
            "This is usually caused by a misconfigured language name",
            logger)

        errors.misconfigured_settings(["development.lang"], logger)

        return False

    path_dest = paths.append_mooncat(path_dest)

    if not paths.can_delete(path_dest):
        errors.tripartite_error(
            "Failed to uninstall library files",
            f"Cannot operate on destination: ({path_dest})",
            "Do you have the right file permissions?",
            logger)

        errors.file_permissions(["write", "execute"], logger)
        return False

    path_dest /= name
    if path_dest.exists():
        paths.remove(path_dest)

    return True

