def create_task(task_list, task):
    task_list.append(task)
    print(f"Task '{task}' added to the list.")

def view_tasks(task_list):
    if not task_list:
        print("No tasks in the list.")
    else:
        print("\n--- To-Do List ---")
        for idx, task in enumerate(task_list, start=1):
            print(f"{idx}. {task}")

def delete_task(task_list, task_number):
    if 0 < task_number <= len(task_list):
        removed_task = task_list.pop(task_number - 1)
        print(f"Task '{removed_task}' removed from the list.")
    else:
        print("Invalid task number! Please try again.")

task_list = []

while True:
    print("\n--- To-Do List App ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ").strip()

    if choice == '1':
        task = input("Enter the task: ")
        create_task(task_list, task)
    elif choice == '2':
        view_tasks(task_list)
    elif choice == '3':
        try:
            task_number = int(input("Enter the task number to delete: "))
            delete_task(task_list, task_number)
        except ValueError:
            print("Please enter a valid number.")
    elif choice == '4':
        print("Exiting the app. Goodbye!")
        break
    else:
        print("Invalid choice! Please try again.")