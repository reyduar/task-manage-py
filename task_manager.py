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
    def __init__(self):
        self.tasks = []
        self.next_id = 1

    def add_task(self, title, description):
        task = Task(self.next_id, title, description)
        self.tasks.append(task)
        self.next_id += 1
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
        print(f"Task with id {task_id} not found")

    def remove_task(self, task_id):
        for item in self.tasks:
            if item.id == task_id:
                self.tasks.remove(item)
                print(f"Task {item.title} removed")
                return
        print(f"Task with id {task_id} not found")
