from typing import Any
from typing import Union

class TType:
    def __getattr__(self, attr: str) -> Any: ...
    def __getitem__(self, item: Any) -> Any: ...
