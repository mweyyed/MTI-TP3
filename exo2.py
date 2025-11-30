# MODEL
class UserModel:
    def __init__(self):
        self.name = ""

    def set_name(self, name):
        self.name = name


# VIEW
class UserView:
    def ask_name(self):
        return input("Enter your name: ")

    def show_greeting(self, name):
        print(f"Hello, {name}! Welcome!")


# CONTROLLER
class UserController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def run(self):
        name = self.view.ask_name()
        self.model.set_name(name)
        self.view.show_greeting(self.model.name)


# MAIN
if __name__ == "__main__":
    model = UserModel()
    view = UserView()
    controller = UserController(model, view)
    controller.run()
