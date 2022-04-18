class Todo:
    """
    This class is the model to represent a to do item.
    """
    def __init__(self, id, title, timestamp, done):
        self.id = id
        self.title = title
        self.timestamp = timestamp
        self.done = done

    def __repr__(self):
        return "<Todo(id={self.id!r})>".format(self=self)
