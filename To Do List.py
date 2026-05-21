print("Welcome To To Do List Application")

to_do_list = []

while True:

    print("\n===== TO DO LIST MENU =====")
    print("1. Add a Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        task_description = input("Enter the task: ")

        task = {
            "description": task_description,
            "completed": False
        }

        to_do_list.append(task)

        print("Task added successfully!")

    elif choice == '2':

        if not to_do_list:
            print("No tasks available.")

        else:
            print("\n===== YOUR TASKS =====")

            for idx, task in enumerate(to_do_list, start=1):

                # Check completion status
                status = "Completed" if task["completed"] else "Pending"

                print(f"{idx}. {task['description']} --> {status}")

    elif choice == '3':

        if not to_do_list:
            print("No tasks available to mark as completed.")

        else:
            print("\n===== TASK LIST =====")

            for idx, task in enumerate(to_do_list, start=1):

                status = "Completed" if task["completed"] else "Pending"

                print(f"{idx}. {task['description']} --> {status}")

            try:
                task_num = int(input("Enter task number to mark as completed: "))

                if 1 <= task_num <= len(to_do_list):

                    to_do_list[task_num - 1]["completed"] = True

                    print("Task marked as completed successfully!")

                else:
                    print("Invalid task number.")

            except ValueError:
                print("Please enter a valid number.")

    elif choice == '4':
        print("Exiting the application. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")