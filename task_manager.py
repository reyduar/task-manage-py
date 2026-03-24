import json


class Task:
    def __init__(self, id, title, description, completed=False):
        self.id = id
        self.title = title
        self.description = description
        self.completed = completed

    def __str__(self):
        status = "(✓)" if self.completed else "(✗)"
        return f"[{status}] #{self.id}: {self.title}"


class TaskManager:
    FILENAME = "tasks.json"

    def __init__(self):
        self.tasks = []
        self.next_id = 1
        self.load_tasks(self.FILENAME)

    def add_task(self, title, description):
        task = Task(self.next_id, title, description)
        self.tasks.append(task)
        self.next_id += 1
        self.save_tasks(self.FILENAME)
        return task

    def list_tasks(self):
        if not self.tasks:
            print("No tasks found")
            return
        for task in self.tasks:
            print(task)

    def mark_task_completed(self, task_id):
        for item in self.tasks:
            if item.id == task_id:
                item.completed = True
                print(f"Task {item.title} marked as completed")
                return
            else:
                print(f"Task with id {task_id} not found")

    def remove_task(self, task_id):
        for item in self.tasks:
            if item.id == task_id:
                self.tasks.remove(item)
                print(f"Task {item.title} removed")
                return
            else:
                print(f"Task with id {task_id} not found")

    def save_tasks(self, filename):
        with open(filename, "w") as f:
            json.dump([task.__dict__ for task in self.tasks], f)

    def load_tasks(self, filename):
        try:
            with open(filename, "r") as f:
                tasks_data = json.load(f)
                self.tasks = [Task(**data) for data in tasks_data]
                if self.tasks:
                    self.next_id = max(task.id for task in self.tasks) + 1
                else:
                    self.next_id = 1
        except FileNotFoundError:
            self.tasks = []
            self.next_id = 1
            print(
                f"No existing task file found at {filename}. Starting with an empty task list.")
