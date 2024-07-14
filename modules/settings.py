from witherlabs.projman import errors, metafile

LANGUAGE = 'development.lang'

def err_setting_not_pressent(setting: str):
    return errors.WLPMError(errors.WLPMErrorType.SETTINGS, f'Option not present in {metafile.path()}: {setting}')
