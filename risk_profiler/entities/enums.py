from enum import Enum


class StringEnum(str, Enum):
    """Base string value enum."""

    def __str__(self):
        return self.value
        
class MaritalStatus(StringEnum):
    single = "single"
    married = "married"

class HouseStatus(StringEnum):
    owned = "owned"
    mortgaged = "mortgaged"

class ScoreLabel(Enum):
    ineligible = "ineligible"
    economic = "economic"
    regular = "regular"
    responsible = "responsible"