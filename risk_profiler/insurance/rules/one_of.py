from .base import Condition
from typing import List


class OneOf(Condition):

    def __init__(self, list: List=[]):
        self.list = list

    def check(self, value:int) -> bool:
        return value in self.list