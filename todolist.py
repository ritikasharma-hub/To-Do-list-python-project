tasks = []

def show_tasks():
    if not tasks:
        print("No event tasks available.")
    else:
        print("My Event Planning To-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def add_task():
    task = input("Enter a new event task: ")
    tasks.append(task)
    print("Event task added!")

def remove_task():
    show_tasks()
    try:
        task_num = int(input("Enter task number to remove: ")) - 1
        if 0 <= task_num < len(tasks):
            tasks.pop(task_num)
            print("Event task removed!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

while True:
    print("\nEvent Planning Menu:")
    print("1. View Event Tasks")
    print("2. Add Event Task")
    print("3. Remove Event Task")
    print("4. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        show_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        remove_task()
    elif choice == "4":
        print("Goodbye! Hope your event goes well! ")
        break
    else:
        print("Invalid choice. Please try again.")