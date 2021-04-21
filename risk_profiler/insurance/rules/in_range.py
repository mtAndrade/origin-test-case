from .base import Condition


class InRange(Condition):

    def __init__(self, min=None, max=None, min_inclusive=True, max_inclusive=True):
        self.min = min
        self.max = max
        self.min_inclusive = min_inclusive
        self.max_inclusive = max_inclusive

    def check(self, value:int) -> bool:
        if self.min is not None and(
            value < self.min if self.min_inclusive else value <= self.min
        ):
            return False
        if self.max is not None and (
            value > self.max if self.max_inclusive else value >= self.max
        ):
           return False

        return True