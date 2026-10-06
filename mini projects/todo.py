tasks = []

while True:

    print("\n--- TO-DO LIST ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":

        task = input("Enter task: ")
        tasks.append(task)

        print("Task added")

    elif choice == "2":

        print("\nYour Tasks:")

        for task in tasks:
            print("-", task)

    elif choice == "3":

        task = input("Enter task to remove: ")

        if task in tasks:
            tasks.remove(task)
            print("Task removed")

        else:
            print("Task not found")

    elif choice == "4":

        print("Goodbye")
        break

    else:
        print("Invalid choice")