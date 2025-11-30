class TaskView:
    def menu(self):
        print("\n=== TASK MANAGER ===")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")
        return input("Choose an option: ")

    def ask_task_info(self):
        title = input("Title: ")
        description = input("Description: ")
        status = input("Status (To Do / In Progress / Completed): ")
        return title, description, status

    def show_tasks(self, tasks):
        print("\n--- Tasks ---")
        if not tasks:
            print("No tasks available.")
            return
        for i, t in enumerate(tasks):
            print(f"{i}. {t.title} | {t.description} | {t.status}")

    def ask_index(self):
        return int(input("Enter task index: "))

    def message(self, msg):
        print(msg)
