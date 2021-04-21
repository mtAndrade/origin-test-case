from .base import Condition


class GreaterThan(Condition):

    def __init__(self, min=None):
        self.min = min

    def check(self, value:int) -> bool:
        return value > self.min