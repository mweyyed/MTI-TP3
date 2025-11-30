from MODEL import TaskModel, Task
from VIEW import TaskView

class TaskController:
    def __init__(self):
        self.model = TaskModel()
        self.view = TaskView()

    def run(self):
        while True:
            choice = self.view.menu()

            if choice == "1":
                title, desc, status = self.view.ask_task_info()
                self.model.add_task(Task(title, desc, status))
                self.view.message("Task added successfully.")

            elif choice == "2":
                self.view.show_tasks(self.model.get_tasks())

            elif choice == "3":
                self.view.show_tasks(self.model.get_tasks())
                index = self.view.ask_index()
                title, desc, status = self.view.ask_task_info()
                if self.model.update_task(index, title, desc, status):
                    self.view.message("Task updated successfully.")
                else:
                    self.view.message("Invalid index.")

            elif choice == "4":
                self.view.show_tasks(self.model.get_tasks())
                index = self.view.ask_index()
                if self.model.delete_task(index):
                    self.view.message("Task deleted.")
                else:
                    self.view.message("Invalid index.")

            elif choice == "5":
                self.view.message("Goodbye!")
                break

            else:
                self.view.message("Invalid choice!")
