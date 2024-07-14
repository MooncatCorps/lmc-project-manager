from typing import Optional
from pathlib import Path
from enum import Enum


class WLPMErrorType(Enum):
    GENERIC = 1,
    FILE = 2,



class WLPMError:

    def __init__(self, etype: WLPMErrorType, reason: str):
        self.etype = etype
        self.reason = reason


class PossibleError[T]:

    def __init__(self, value: Optional[T]):
        self.value = value
        self.error_count: int = 0
        self.errors: list[WLPMError] = []


def non_existent_path(path: Path):
    return WLPMError(WLPMErrorType.FILE, f'Path does not exist: {path}')
