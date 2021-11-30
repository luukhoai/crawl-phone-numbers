from marshmallow import fields, validate

from ..common.schema import BaseSchema


class AddressQuerySchema(BaseSchema):
    '''Schema to validate query input'''
    address = fields.String(
        required=True, validate=validate.Length(min=1, max=100))
