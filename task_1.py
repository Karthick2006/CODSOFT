tasks = []

def show_menu():
    print("\n==== TO-DO LIST MENU ====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")

def add_task():
    task = input("Enter the task: ")
    tasks.append({"task": task, "completed": False})
    print("✅ Task added!")

def view_tasks():
    if not tasks:
        print("📭 No tasks found.")
        return
    print("\n📋 Your Tasks:")
    for idx, task in enumerate(tasks, 1):
        status = "✅" if task["completed"] else "❌"
        print(f"{idx}. [{status}] {task['task']}")

def mark_completed():
    view_tasks()
    if tasks:
        try:
            num = int(input("Enter task number to mark as completed: "))
            if 1 <= num <= len(tasks):
                tasks[num-1]["completed"] = True
                print("✅ Task marked as completed!")
            else:
                print("⚠️ Invalid task number.")
        except ValueError:
            print("⚠️ Please enter a valid number.")

def delete_task():
    view_tasks()
    if tasks:
        try:
            num = int(input("Enter task number to delete: "))
            if 1 <= num <= len(tasks):
                removed = tasks.pop(num-1)
                print(f"🗑️ Task '{removed['task']}' deleted!")
            else:
                print("⚠️ Invalid task number.")
        except ValueError:
            print("⚠️ Please enter a valid number.")

while True:
    show_menu()
    choice = input("Choose an option (1-5): ")
    if choice == '1':
        add_task()
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        mark_completed()
    elif choice == '4':
        delete_task()
    elif choice == '5':
        print("👋 Exiting To-Do List. Goodbye!")
        break
    else:
        print("⚠️ Invalid choice. Try again.")
