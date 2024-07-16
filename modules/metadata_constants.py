from witherlabs.projman.error_handling import Maybe


ORGANIZATION_NAME = 'witerlabs'


def err_required_option_not_present(parent_setting: str, setting: str) -> Maybe:
    return Maybe(None, f'Option not present in {parent_setting}: {setting}')
