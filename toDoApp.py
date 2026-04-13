def create_task(task_list, task):
    task_list.append(task)
    print(f"Task '{task}' added to the list.")

def view_tasks(task_list):
    if not task_list:
        print("No tasks in the list.")
    else:
        print("\n--- To-Do List ---")
        for idx, task in enumerate(task_list, start=1):
            print(f"{idx + 1}. {task}")

def delete_task(task_list, task_number):
    if 0 < task_number <= len(task_list):
        removed_task = task_list.pop(task_number - 1)
        print(f"Task '{removed_task}' removed from the list.")
    else:
        print("Invalid task number! Please try again.")