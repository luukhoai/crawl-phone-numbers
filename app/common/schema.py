from marshmallow import EXCLUDE
from marshmallow.schema import Schema


class BaseSchema(Schema):

    class Meta:
        unknown = EXCLUDE
