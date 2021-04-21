from .base import Condition
from typing import Any

class NotExists(Condition):

    def check(self, value:Any) -> bool:
        return value is None