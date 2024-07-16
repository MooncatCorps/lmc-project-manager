from typing import Generic, Optional, TypeVar

MaybeType = TypeVar('MaybeType')
class Maybe(Generic[MaybeType]):

    def __init__(self, value: Optional[MaybeType], error_reason: Optional[str] = None):
        if value is None and error_reason is None:
            raise ValueError('`Value` and `Reason` may not both be `None` in a `Maybe` type')

        self.value = value
        self.error_reason = error_reason

    def contains_value(self) -> bool:
        return (self.error_reason is None) and (self.value is not None)

    def contains_error(self) -> bool:
        return not self.contains_value()

    def get_value(self) -> MaybeType:
        if self.contains_error():
            raise ValueError(f'Attempted to access a `Maybe` object\'s value while an error is present: {self.error_reason}')

        assert self.value is not None
        return self.value

    def get_error(self) -> str:
        if self.contains_value():
            raise ValueError('Attempted to access a `Maybe` object\'s error while none is present')

        assert self.error_reason is not None
        return self.error_reason

