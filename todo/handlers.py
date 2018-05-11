from todo.entities import Task


class AddNewTaskHandler(object):

    def __init__(self, repository):
        self.repository = repository

    def handle(self, command):
        task = Task(
            title=command.title,
            description=command.description
        )
        self.repository.save(task)
