tasks = []


while True:
    print("\n1: Add a task ")
    print("2: View tasks")
    print("3: Remove a task")
    print("4: Mark a task as complete")
    print("5: Quit")

    options = input("Choose an option (1-5): ")

    if options == "1":
        #Add a task
        def add_task(tasks):
            task_name = (input("Enter the task: "))
            tasks.append({"task":task_name,"completed":False })
            print(f"Task '{task_name}' added successfully!")
        add_task(tasks)

    elif options == "2":
        #View tasks
        def view_task(tasks):
            if tasks == []:
                print("Congrats! There are currently no tasks!")
            else:
                print("\nTo do list: ")
                for idx, task in enumerate(tasks, start=1):
                    status = "[x]" if task["completed"] else "[ ]"
                    print(f"{idx}. {status} {task['task']}")
        view_task(tasks)

    elif options == "3":
        #Remove a task
        def remove_task(tasks):
            view_task(tasks) #shows the list to help the user choose
            try:
                task_num = int(input("Enter the task number to remove: ")) - 1
                if 0 <= task_num < len(tasks):
                    removed_task = tasks.pop(task_num)
                    print(f"Removed task: '{removed_task['task']}'")
                else:
                    print(("Invalid task number."))
            except ValueError:
                print("Please enter a valid number.")
        remove_task(tasks) 

    elif options == "4":
        #Mark a task as complete
        def mark_task_complete(tasks):
            view_task(tasks) #Show the list to help the user choose
            try: 
                task_num = int(input("Enter the task number to mark as complete: ")) - 1
                if 0 <= task_num < len(tasks):
                    tasks[task_num]["completed"] = True
                    print(f"Marked task '{tasks[task_num]['task']}' ad complete!")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")
        mark_task_complete(tasks)

    elif options == "5":
        #Quit
        print("Have a great day! Goodbye!")
        break

    else:
        print("Sorry! You did not enter a valid option.")
        options = int(input("What would u like to do (1-5): "))
