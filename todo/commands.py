class AddNewTask(object):

    def __init__(self, title, description):
        self.title = title
        self.description = description


class UpdateTask(object):

    def __init__(self, identifier, title, description):
        self.identifier = identifier
        self.title = title
        self.description = description
