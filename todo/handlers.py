import marshmallow

from todo.entities import Task
from todo.schemas import TaskSchema


class ValidationError(Exception):
    def __init__(self, errors):
        self.errors = errors

class AddNewTaskHandler(object):

    def __init__(self, repository):
        self.repository = repository

    def handle(self, command):
        try:
            TaskSchema().load(
                {'title': command.title,
                'description': command.description}
            )        
        except marshmallow.ValidationError as errors:
            return ValidationError(errors)

        task = Task(
            title=command.title,
            description=command.description
        )
        self.repository.save(task)
