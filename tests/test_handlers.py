import pytest

from todo.commands import AddNewTask
from todo.handlers import AddNewTaskHandler, ValidationError


class FakeTaskRepository(object):

    def __init__(self):
        self.tasks = []

    def count(self):
        return len(self.tasks)

    def save(self, task):
        self.tasks.append(task)


def test_add_new_task():
    repository = FakeTaskRepository()
    handler = AddNewTaskHandler(repository=repository)
    command = AddNewTask(
        title='Buy milk', 
        description='Need to buy 2L of milk'
    )
    handler.handle(command)
    assert repository.count() == 1

def test_add_new_test_without_required_fields():
    repository = FakeTaskRepository()
    handler = AddNewTaskHandler(repository=repository)
    command = AddNewTask(
        title='', 
        description=''
    )
    with pytest.raises(ValidationError) as error:
        handler.handle(command)

    errors = error.value.errors

    assert errors['title'] == ['Length must be between 1 and 50.']
    assert errors['description'] == ['Length must be between 1 and 150.']

def test_add_new_task_start_as_not_completed():
    repository = FakeTaskRepository()
    handler = AddNewTaskHandler(repository=repository)
    command = AddNewTask(
        title='Buy milk', 
        description='Need to buy 2L of milk'
    )
    task = handler.handle(command)

    assert task.completed == False
