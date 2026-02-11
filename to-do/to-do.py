import json
import os

class Task:
    def __init__(self, task_id, title, completed=False):
        self.id = task_id
        self.title = title
        self.completed = completed

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "completed": self.completed
        }

    @staticmethod
    def from_dict(data):
        return Task(data["id"], data["title"], data["completed"])



class TodoManager:
    FILE_NAME = "todos.json"

    def __init__(self):
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.FILE_NAME):
            with open(self.FILE_NAME, "r") as file:
                data = json.load(file)
                self.tasks = [Task.from_dict(task) for task in data]

    def save_tasks(self):
        with open(self.FILE_NAME, "w") as file:
            json.dump([task.to_dict() for task in self.tasks], file, indent=4)

    def add_task(self, title):
        task_id = len(self.tasks) + 1
        self.tasks.append(Task(task_id, title))
        self.save_tasks()

    def view_tasks(self):
        if not self.tasks:
            print("\nNo tasks found.\n")
            return

        for task in self.tasks:
            status = "✔ Done" if task.completed else "❌ Not Done"
            print(f"{task.id}. {task.title} - {status}")

    def update_task(self, task_id, new_title=None, completed=None):
        for task in self.tasks:
            if task.id == task_id:
                if new_title:
                    task.title = new_title
                if completed is not None:
                    task.completed = completed
                self.save_tasks()
                return
        print("Task not found.")

    def delete_task(self, task_id):
        self.tasks = [task for task in self.tasks if task.id != task_id]

        # Reassign IDs
        for i, task in enumerate(self.tasks):
            task.id = i + 1

        self.save_tasks()


def main():
    manager = TodoManager()

    while True:
        print("\n==== TODO APP ====")
        print("1. Add Todo")
        print("2. View Todos")
        print("3. Update Todo")
        print("4. Delete Todo")
        print("5. Exit")

        choice = input("Choose: ")

        if choice == "1":
            title = input("Enter task title: ")
            manager.add_task(title)
            print("Task added!")

        elif choice == "2":
            manager.view_tasks()

        elif choice == "3":
            task_id = int(input("Enter task ID: "))
            print("1. Change title")
            print("2. Mark completed")
            print("3. Mark not completed")

            option = input("Choose: ")

            if option == "1":
                new_title = input("New title: ")
                manager.update_task(task_id, new_title=new_title)

            elif option == "2":
                manager.update_task(task_id, completed=True)

            elif option == "3":
                manager.update_task(task_id, completed=False)

        elif choice == "4":
            task_id = int(input("Enter task ID to delete: "))
            manager.delete_task(task_id)
            print("Task deleted!")

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()