from abc import ABC, abstractmethod
from typing import Any


class Condition(ABC):
        
    @abstractmethod
    def check(self, value: Any ) -> bool:
        pass
