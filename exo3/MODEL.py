
class Task:
    def __init__(self, title, description, status="To Do"):
        self.title = title
        self.description = description
        self.status = status


class TaskModel:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def get_tasks(self):
        return self.tasks

    def update_task(self, index, title=None, description=None, status=None):
        if 0 <= index < len(self.tasks):
            if title:
                self.tasks[index].title = title
            if description:
                self.tasks[index].description = description
            if status:
                self.tasks[index].status = status
            return True
        return False

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)
            return True
        return False
