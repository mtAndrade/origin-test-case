from .enums import HouseStatus


class House:

    ownership_status : HouseStatus

    def __init__(self, ownership_status=None):
        self.ownership_status = ownership_status