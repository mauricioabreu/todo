from marshmallow import Schema, fields


class TaskSchema(Schema):
    title = fields.Str()
    description = fields.Str()
