import json
import sys

TASKS_FILE = "tasks.json"

def load_tasks():
    """Loads tasks from the tasks.json file."""
    try:
        with open(TASKS_FILE, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        # Return an empty list if file doesn't exist or is empty/corrupted
        return []

def save_tasks(tasks):
    """Saves the list of tasks to the tasks.json file."""
    with open(TASKS_FILE, 'w') as f:
        json.dump(tasks, f, indent=4)

def view_tasks(tasks):
    """Displays the list of tasks."""
    if not tasks:
        print("\nYour to-do list is empty!")
        return
    
    print("\n---------- To-Do List ----------")
    for index, task_item in enumerate(tasks, start=1):
        status_icon = "✓" if task_item['status'] == 'done' else " "
        print(f"{index}. [{status_icon}] {task_item['task']}")
    print("--------------------------------")

def add_task(tasks):
    """Adds a new task to the list."""
    task_name = input("Enter the task description: ")
    if task_name.strip(): # Ensure task is not empty
        new_task = {"task": task_name, "status": "pending"}
        tasks.append(new_task)
        save_tasks(tasks)
        print(f"\nTask '{task_name}' added successfully.")
    else:
        print("\nTask description cannot be empty.")
    
def delete_task(tasks):
    """Deletes a task from the list."""
    view_tasks(tasks)
    if not tasks: return

    try:
        task_number_str = input("Enter the task number to delete: ")
        task_number = int(task_number_str)
        
        if 1 <= task_number <= len(tasks):
            # Store task name before removing for the message
            removed_task = tasks.pop(task_number - 1)
            save_tasks(tasks)
            print(f"\nTask '{removed_task['task']}' deleted successfully.")
        else:
            print("\nInvalid task number.")
    except ValueError:
        print("\nInvalid input. Please enter a number.")

def update_task(tasks):
    """Marks a task's status as done."""
    view_tasks(tasks)
    if not tasks: return
    
    try:
        task_number_str = input("Enter the task number to mark as done: ")
        task_number = int(task_number_str)

        if 1 <= task_number <= len(tasks):
            tasks[task_number - 1]["status"] = "done"
            save_tasks(tasks)
            print(f"\nTask {task_number} marked as done successfully.")
        else:
            print("\nInvalid task number.")
    except ValueError:
        print("\nInvalid input. Please enter a number.")

if __name__ == "__main__":
    tasks = load_tasks()
    
    print("\nWelcome to your Interactive To-Do List")
    
    while True:
        print("\n--- Menu ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Mark Task as Done")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            update_task(tasks)
        elif choice == "5":
            print("Goodbye!")
            sys.exit()
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")