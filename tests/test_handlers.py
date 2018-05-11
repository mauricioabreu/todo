from todo.commands import AddNewTask
from todo.handlers import AddNewTaskHandler


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
