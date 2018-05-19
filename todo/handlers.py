import marshmallow

from todo.entities import Task, Project
from todo.schemas import TaskSchema


class ValidationError(Exception):
    def __init__(self, errors):
        self.errors = errors


class AddNewTaskHandler(object):

    def __init__(self, repository):
        self.repository = repository

    def handle(self, command):
        schema = TaskSchema()
        errors = schema.validate({
            'title': command.title,
            'description': command.description,
            'project_id': command.project_id
        })

        if errors:
            raise ValidationError(errors=errors)

        project = Project(name='Daily stuff')
        task = Task(
            title=command.title,
            description=command.description,
            completed=False,
            project=project
        )
        self.repository.save(task)

        return task


class UpdateTaskHandler(object):

    def __init__(self, repository):
        self.repository = repository

    def handle(self, command):
        schema = TaskSchema()
        errors = schema.validate({
            'title': command.title,
            'description': command.description
        })

        if errors:
            raise ValidationError(errors=errors)

        task = self.repository.find_by_id(task_id=command.identifier)
        task.title = command.title
        task.description = command.description

        self.repository.save(task, command.identifier)
