from todo import add_task, view_tasks, mark_complete, delete_task

def menu():
    print("\nSmart To-Do Manager")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")

while True:
    menu()
    choice = input("Choose an option: ")

    if choice == "1":
        title = input("Enter task title: ")
        add_task(title)
        print("Task added.")

    elif choice == "2":
        tasks = view_tasks()
        for i, task in enumerate(tasks):
            status = "✔" if task["completed"] else "✘"
            print(f"{i}. {task['title']} [{status}]")

    elif choice == "3":
        index = int(input("Enter task index: "))
        mark_complete(index)
        print("Task marked as completed.")

    elif choice == "4":
        index = int(input("Enter task index: "))
        delete_task(index)
        print("Task deleted.")

    elif choice == "5":
        break

    else:
        print("Invalid choice.")
