tasks = []

def display_tasks():
    if not tasks:
        print("Your To-Do List is empty.")
    else:
        print("To-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def add_task(task):
    tasks.append(task)
    print(f"Task '{task}' added to your To-Do List.")

def remove_task(task_index):
    if 1 <= task_index <= len(tasks):
        removed_task = tasks.pop(task_index - 1)
        print(f"Task '{removed_task}' removed from your To-Do List.")
    else:
        print("Invalid task number. Task not removed.")

while True:
    print("\nOptions:")
    print("1. Display To-Do List")
    print("2. Add a Task")
    print("3. Remove a Task")
    print("4. Quit")

    choice = input("Enter your choice: ")

    if choice == '1':
        display_tasks()
    elif choice == '2':
        task = input("Enter the task you want to add: ")
        add_task(task)
    elif choice == '3':
        display_tasks()
        task_index = int(input("Enter the task number you want to remove: "))
        remove_task(task_index)
    elif choice == '4':
        print("Goodbye, Thank You For Using !")
        break
    else:
        print("Invalid choice. Please select a valid option.")
