import pytest

from todo.commands import AddNewTask, UpdateTask
from todo.exceptions import ObjectNotFound
from todo.handlers import AddNewTaskHandler, UpdateTaskHandler, ValidationError


class FakeTaskRepository(object):

    def __init__(self):
        self.tasks = {}
        self.last_id = None

    def count(self):
        return len(self.tasks)

    def save(self, task, identifier=None):
        task_id = identifier or self.next_id()
        self.tasks[task_id] = task

    def find_by_id(self, task_id):
        try:
            return self.tasks[task_id]
        except KeyError:
            raise ObjectNotFound

    def all(self):
        return self.tasks

    def next_id(self):
        if not self.last_id:
            self.last_id = 1
        else:
            self.last_id = self.last_id + 1

        return self.last_id


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

    assert task.completed is False


def test_update_task():
    repository = FakeTaskRepository()
    handler = AddNewTaskHandler(repository=repository)
    command = AddNewTask(
        title='Buy milk',
        description='Need to buy 2L of milk'
    )
    handler.handle(command)

    handler = UpdateTaskHandler(repository=repository)
    command = UpdateTask(
        identifier=1,
        title='Write for my blog',
        description='I will talk about my last projects'
    )
    handler.handle(command)

    task = repository.find_by_id(1)
    assert task.title == 'Write for my blog'
    assert task.description == 'I will talk about my last projects'
    assert repository.count() == 1


def test_update_invalid_task():
    repository = FakeTaskRepository()
    handler = UpdateTaskHandler(repository=repository)
    command = UpdateTask(
        identifier=1,
        title='Write for my blog',
        description='I will talk about my last projects'
    )
    with pytest.raises(ObjectNotFound):
        handler.handle(command)
