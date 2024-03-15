tasks = []


def add_task():
    name = input("\nEnter task name: ")
    priority = input("Enter task priority: ")
    due_date = input("Enter task due date (YYYY-MM-DD): ")
    tasks.append(
        {
            "name": name,
            "priority": priority,
            "due_date": due_date,
            "status": "Incomplete",
        }
    )


def remove_task():
    name = input("\nEnter task name to remove: ")
    tasks[:] = [task for task in tasks if task["name"] != name]


def mark_as_complete():
    name = input("\nEnter task name to mark as complete: ")
    for task in tasks:
        if task["name"] == name:
            task["status"] = "Complete"


def list_tasks():
    if not tasks:
        print("\nThere are no tasks.")
    else:
        print()
        for task in tasks:
            print(
                f"Name: {task['name']}, Priority: {task['priority']}, Due date: {task['due_date']}, Status: {task['status']}"
            )


def main():
    while True:
        print("\n1. Add task")
        print("2. Remove task")
        print("3. Mark task as complete")
        print("4. List tasks")
        print("5. Exit")
        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            remove_task()
        elif choice == "3":
            mark_as_complete()
        elif choice == "4":
            list_tasks()
        elif choice == "5":
            break
        else:
            print("\nInvalid choice. Please choose a valid option.")


if __name__ == "__main__":
    main()
