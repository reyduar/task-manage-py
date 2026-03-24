from task_manager import TaskManager


def print_menu():
    print("\nTask Manager")
    print("1. Add Task")
    print("2. List Tasks")
    print("3. Mark Task as Completed")
    print("4. Remove Task")
    print("5. Exit")


def main():
    task_manager = TaskManager()
    while True:
        print_menu()

        choice = input("Enter your choice: ")
        match choice:
            case "1":
                title = input("Enter the title of the task: ")
                description = input("Enter the description of the task: ")
                task_manager.add_task(title, description)
            case "2":
                task_manager.list_tasks()
            case "3":
                task_id = input(
                    "Enter the ID of the task to mark as completed: ")
                try:
                    task_manager.mark_task_completed(task_id)
                except ValueError:
                    print("Invalid input. Please enter a valid task ID.")

            case "4":
                task_id = input("Enter the ID of the task to remove: ")
                try:
                    task_manager.remove_task(task_id)
                except ValueError:
                    print("Invalid input. Please enter a valid task ID.")
            case "5":
                print("Exiting...")
                break
            case _:
                print("Invalid choice")


if __name__ == "__main__":
    main()
