from witherlabs.projman import metafile
from typing import Generic, Optional, TypeVar
from pathlib import Path
from enum import Enum


class WLPMErrorType(Enum):
    GENERIC = 1,
    FILE = 2,
    SETTINGS= 3,
    LANGUAGE = 4,



class WLPMError:

    def __init__(self, etype: WLPMErrorType, reason: str):
        self.etype = etype
        self.reason = reason

__T = TypeVar('__T')
class PossibleError(Generic[__T]):

    def __init__(self, value: Optional[__T]):
        self.value = value
        self.error_count: int = 0
        self.errors: list[WLPMError] = []


    def add_error(self, err: WLPMError):
        self.errors.append(err)


    def set_value(self, value: __T):
        self.value = value


    def has_errors(self) -> bool:
        return self.error_count > 0


def non_existent_path(path: Path):
    return WLPMError(WLPMErrorType.FILE, f'Path does not exist: {path}')


