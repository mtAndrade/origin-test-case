from marshmallow import Schema, fields, validate, post_load
from risk_profiler.entities.enums import HouseStatus
from risk_profiler.entities.house import House

class HouseSchema(Schema):
    ownership_status = fields.Str(required=True, validate=validate.OneOf(list(HouseStatus)))
        
    @post_load
    def make_house(self, data, **kwargs):
        return House(**data)