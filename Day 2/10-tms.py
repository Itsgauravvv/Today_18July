def add_task(tasks):
    task = input("Enter Task Name: ")
    tasks.append(task)
    print("Task added successfully.")


def view_tasks(tasks):
    if len(tasks) == 0:
        print("No tasks available.")
    else:
        print("\nProject Tasks")
        for i in range(len(tasks)):
            print(f"{i+1} - {tasks[i]}")


def search_task(tasks):
    task = input("Enter Task Name to Search: ")

    if task in tasks:
        print("Task Found.")
    else:
        print("Task Not Found.")


def update_task(tasks):
    if len(tasks) == 0:
        print("No tasks available.")
        return

    view_tasks(tasks)

    task_no = int(input("Enter Task Number: "))

    if 1 <= task_no <= len(tasks):
        new_task = input("Enter New Task: ")
        tasks[task_no - 1] = new_task
        print("Task updated successfully.")
    else:
        print("Invalid Task Number.")


def delete_task(tasks):
    if len(tasks) == 0:
        print("No tasks available.")
        return

    view_tasks(tasks)

    task_no = int(input("Enter Task Number: "))

    if 1 <= task_no <= len(tasks):
        tasks.pop(task_no - 1)
        print("Task deleted successfully.")
    else:
        print("Invalid Task Number.")


def count_tasks(tasks):
    print("Total Project Tasks:", len(tasks))


tasks = []

while True:

    print("\n========== Project Task Management System ==========")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Search Task")
    print("4. Update Task")
    print("5. Delete Task")
    print("6. Count Tasks")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_task(tasks)

    elif choice == 2:
        view_tasks(tasks)

    elif choice == 3:
        search_task(tasks)

    elif choice == 4:
        update_task(tasks)

    elif choice == 5:
        delete_task(tasks)

    elif choice == 6:
        count_tasks(tasks)

    elif choice == 7:
        print("Exiting Program...")
        break

    else:
        print("Invalid Choice!")