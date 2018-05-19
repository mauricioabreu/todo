class AddNewProject(object):

    def __init__(self, name):
        self.name = name


class AddNewTask(object):

    def __init__(self, title, description, project_id):
        self.title = title
        self.description = description
        self.project_id = project_id


class UpdateTask(object):

    def __init__(self, identifier, title, description):
        self.identifier = identifier
        self.title = title
        self.description = description
