class Project(object):

    def __init__(self, name):
        self.name = name


class Task(object):

    def __init__(self, title, description, completed, project):
        self.title = title
        self.description = description
        self.completed = completed
        self.project = project
