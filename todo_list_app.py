# todo_list_app.py

TASK_FILE = "todo.txt"

# Load tasks from file into a list
def load_tasks():
    try:
        with open(TASK_FILE, "r") as file:
            tasks = [line.strip() for line in file.readlines()]
        return tasks
    except FileNotFoundError:
        return []

# Save task list to file
def save_tasks(tasks):
    with open(TASK_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")

# Display all tasks
def view_tasks(tasks):
    if not tasks:
        print("Your to-do list is empty.\n")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
        print()

# Add a new task
def add_task(tasks):
    task = input("Enter new task: ").strip()
    if task:
        tasks.append(task)
        save_tasks(tasks)
        print("Task added!\n")
    else:
        print("Empty task not added.\n")

# Remove a task by number
def remove_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    try:
        index = int(input("Enter task number to remove: "))
        if 1 <= index <= len(tasks):
            removed = tasks.pop(index - 1)
            save_tasks(tasks)
            print(f"Removed: {removed}\n")
        else:
            print("Invalid task number.\n")
    except ValueError:
        print("Please enter a valid number.\n")

# Main menu loop
def main():
    tasks = load_tasks()
    while True:
        print("==== To-Do List Menu ====")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")
        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.\n")

if __name__ == "__main__":
    main()
