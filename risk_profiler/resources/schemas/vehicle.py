from marshmallow import Schema, fields, validate, post_load
from risk_profiler.entities.vehicle import Vehicle

class VehicleSchema(Schema):
    year = fields.Int(required=True, validate=validate.Range(min=1769))

    @post_load
    def make_vehicle(self, data, **kwargs):
        return Vehicle(**data)