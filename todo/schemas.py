from marshmallow import Schema, fields
from marshmallow.validate import Length


class TaskSchema(Schema):
    class Meta:
        strict = True
        
    title = fields.String(
        required=True, 
        validate=[Length(min=1, max=50)]
    )
    description = fields.String(
        required=True,
        validate=[Length(min=1, max=150)]
    )
