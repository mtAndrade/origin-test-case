from risk_profiler.insurance.rules.base import Condition
from abc import ABC, abstractmethod
from typing import Any, Optional

class ChainScoreRule:

    _value: Any
    _score: int
    _update_score: bool
    _broken_chain: bool

    def __init__(self, score: int = 0, update_score:bool = False):
        self._score = score
        self._update_score = update_score
        self._broken_chain = False

    def when(self, value: Any, condition: Condition):
        self._value = value
        self._update_score = condition.check(self._value)
        return self
    
    def add(self, value:int):
        if(self._update_score and not self._broken_chain):
            self._score = self._score + value
        self._update_score = False

        return self

    def subtract(self, value:int):
        if(self._update_score and not self._broken_chain):
            self._score = self._score - value
        self._update_score = False

        return self

    def disable(self) -> str:
        if(not self._broken_chain):
            self._broken_chain = self._update_score 
            self._update_score = False
        return self
    
    def process(self):
        if(self._broken_chain):
            return None
        return self._score