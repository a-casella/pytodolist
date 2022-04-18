from marshmallow import Schema, fields, post_load

from classes.Todo import Todo


class TodoSchema(Schema):
    """
    This class is the schema for serializing and deserializing.
    """
    id = fields.Int()
    title = fields.Str()
    timestamp = fields.Int()
    done = fields.Bool()

    @post_load
    def make_todo(self, data, **kwargs):
        """
        This method is called after the deserialization and receives the deserialized data as input. It returns
         a new T odo
        :param data: the deserialized data
        :param kwargs: the keyword arguments
        :return: the new T odo
        """
        return Todo(**data)

