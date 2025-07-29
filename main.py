import json
import sys

TASKS_FILE = "tasks.json"

def load_task():
    try:
        with open(TASKS_FILE, "r") as f:
            return json.load(f)
    
    except FileNotFoundError:
        return []
    
    except json.JSONDecodeError:
        return []

def view_tasks(tasks):
    if not tasks:
        print("No tasks found")
        return
    
    print("\n-----------------To Do List-----------------")
    for index,task in enumerate(tasks,start=1):
        status = "done" if task['status'] == 'done' else "pending"
        print(f"{index}. {task['task']} [{status}]")
    print("--" * 20)

def add_task(tasks):
    new_task = {"task":input("Enter task: "),"status":"pending"}
    tasks.append(new_task)
    save_task(tasks)
    print(f"Task : {new_task} added successfully.")
    
def delete_task(tasks):
    view_tasks(tasks)
    task_number = int(input("Enter task number to delete: "))
    tasks.pop(task_number - 1)
    save_task(tasks)
    print(f"Task {tasks[task_number]} deleted successfully.")

def update_task(tasks):
    view_tasks(tasks)
    task_number = int(input("Enter task number to mark as done: "))
    tasks[task_number - 1]["status"] = "done"
    save_task(tasks)
    print(f"Task {task_number} marked as done successfully.")

def save_task(tasks):
    with open(TASKS_FILE,'w') as f:
        json.dump(tasks,f,indent=4)
        
if __name__ == "__main__":
    tasks = load_task()
    
    print("\n Welcome to the CLI-To-Do-List")
    print("--" * 20)
    while True:
        print("\n1. View Tasks\n2. Add Task\n3. Delete Task\n4. Mark Task as Done\n5. Exit\n")
        choice = input("Enter your choice: ")
        
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
            print("Invalid choice. Please try again.")