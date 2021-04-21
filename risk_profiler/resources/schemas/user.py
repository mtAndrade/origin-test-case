from marshmallow import Schema, fields, validate, post_load, ValidationError
from risk_profiler.entities.enums import MaritalStatus
from risk_profiler.entities.user import User
from .house import HouseSchema
from .vehicle import VehicleSchema



class UserSchema(Schema):
    age = fields.Int(required=True, validate=validate.Range(min=0), strict=True)
    dependents = fields.Int(required=True, validate=validate.Range(min=0), strict=True)
    income = fields.Int(required=True, validate=validate.Range(min=0), strict=True)

    marital_status = fields.Str(required=True, validate=validate.OneOf(list(MaritalStatus)))
    risk_questions = fields.List(fields.Integer(required=True, strict=True, validate=validate.OneOf([0,1])), required=True)

    house = fields.Nested(HouseSchema, required=True)
    vehicle = fields.Nested(VehicleSchema, required=True)

    @post_load
    def make_user(self, data, **kwargs):
        if("risk_questions" in data and len(data["risk_questions"]) !=3 ):
            raise ValidationError(message=['Risk questions should be a list with 3 entries'],
                                      field_name='risk_questions')
        return User(**data)