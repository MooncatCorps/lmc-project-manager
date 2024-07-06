from witherlabs.projman import paths, errors
import os
import logging


def install_library_files(name: str, lang: str, logger: logging.Logger, dev: bool = False) -> bool:
    logger.debug('Performing library installation')

    path_from = paths.internal_library_files(lang)
    path_base = paths.external_library_files(lang)

    logger.debug(f'Source Path: {path_from}')
    logger.debug(f'Base Destination Path: {path_base}')

    if path_base == None:
        errors.misconfiguration('Could not determine library install path',
                                { 'development.lang' : 'Helps determine installation destination directory'},
                                logger)
        return False


    if not path_base.exists():
        logger.error('Missing library install location')
        errors.file_not_found(path_base, logger)
        return False


    if not paths.has_access(path_base):
        errors.insufficient_file_permissions(path_base, ['read', 'write', 'execute'], logger)
        return False

    if path_from == None:
        errors.misconfiguration('Could not determine library install source',
                                { 'development.lang' : 'Helps determine installation source directory'},
                                logger)
        return False

    if not path_from.exists():
        logger.error('Missing library install source')
        errors.file_not_found(path_base, logger)
        logger.info(f'Your library file directory should be named \'{path_from.name}\'')
        return False

    if not paths.can_read(path_from):
        errors.insufficient_file_permissions(path_from, ['read'], logger)
        return False

    path_wither = paths.append_namespace(path_base)
    path_lib = path_wither/name

    logger.debug(f'WitherLabs Destination Path: {path_wither}')
    logger.debug(f'Library Destination Path: {path_lib}')

    logger.debug(f'Attempting to create path: {path_wither}')
    os.makedirs(path_wither, exist_ok = True)

    if not paths.has_access(path_wither):
        errors.insufficient_file_permissions(path_wither, ['read', 'write', 'execute'], logger)
        return False

    if path_lib.exists():
        logger.debug(f'Cleaning up: {path_base}')
        paths.remove(path_lib)

    logger.debug(f'Copying {path_from} to {path_base}; Symlink = {dev}')
    paths.copy(path_from, path_lib, symlink = dev)

    logger.debug(f'Done')
    return True


def uninstall_library_files(name: str, lang: str, logger: logging.Logger) -> bool:
    logger.debug('Performing library uninstallation')

    path_base = paths.external_library_files(lang)

    logger.debug(f'Base Destination Path: {path_base}')

    if path_base == None:
        errors.misconfiguration('Could not determine library uninstall path',
                                { 'development.lang' : 'Helps determine (un)installation destination directory'},
                                logger)
        return False


    if not path_base.exists():
        logger.error('Missing library uninstall target')
        logger.info('This usually means that there is nothing to uninstall')
        errors.file_not_found(path_base, logger)
        return False


    if not paths.has_access(path_base):
        errors.insufficient_file_permissions(path_base, ['read', 'write', 'execute'], logger)
        return False

    path_wither = paths.append_namespace(path_base)
    path_lib = path_wither/name

    logger.debug(f'WitherLabs Destination Path: {path_wither}')
    logger.debug(f'Library Destination Path: {path_lib}')

    if not path_wither.exists():
        errors.file_not_found(path_wither, logger)
        logger.info('This usually means that there is nothing to uninstall (at all)')
        return False

    if not paths.has_access(path_wither):
        errors.insufficient_file_permissions(path_wither, ['read', 'write', 'execute'], logger)
        return False

    if path_lib.exists():
        logger.debug(f'Removing: {path_lib}')
        paths.remove(path_lib)
    else:
        errors.file_not_found(path_lib, logger)
        logger.info('This usually means that there is nothing to uninstall')
        return False

    logger.debug(f'Done')
    return True
