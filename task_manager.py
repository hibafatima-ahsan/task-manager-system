from task import Task
from project_task import ProjectTask
from file_handler import load_tasks, save_tasks


# ----------------------------
# Add Task
# ----------------------------
def add_task():

    tasks = load_tasks()

    print("\n1. Normal Task")
    print("2. Project Task")

    task_type = input("Choose Task Type: ")

    task_id = input("Task ID: ")
    for existing in tasks:
        if existing.get("task_id") == task_id:
            print(f"Task ID '{task_id}' already exists! Creation aborted.")
            return

    title = input("Title: ")
    description = input("Description: ")
    assigned_to = input("Assigned To: ")

    while True:
        try:
            priority = int(input("Priority (1-5): "))

            if 1 <= priority <= 5:
                break

            print("Priority must be between 1 and 5.")

        except ValueError:
            print("Invalid Priority!")

    status = "Pending"

    if task_type == "2":

        project_name = input("Project Name: ")
        deadline = input("Deadline: ")

        task = ProjectTask(
            task_id=task_id,
            title=title,
            description=description,
            assigned_to=assigned_to,
            priority=priority,
            status=status,
            deadline=deadline,
            project_name=project_name
        )

        data = task.to_dict()

    else:

        task = Task(
            task_id=task_id,
            title=title,
            description=description,
            assigned_to=assigned_to,
            priority=priority,
            status=status
        )

        data = task.to_dict()

    tasks.append(data)

    save_tasks(tasks)

    print("\nTask Added Successfully!")


# ----------------------------
# View All Tasks
# ----------------------------
def view_tasks():

    tasks = load_tasks()

    if not tasks:
        print("\nNo Tasks Found!")
        return

    print("\n========== TASKS ==========\n")

    for task in tasks:

        print(f"Task ID      : {task['task_id']}")
        print(f"Title        : {task['title']}")
        print(f"Description  : {task['description']}")
        print(f"Assigned To  : {task['assigned_to']}")
        print(f"Priority     : {task['priority']}")
        print(f"Status       : {task['status']}")

        if task.get("type") == "project" or ("project_name" in task and "deadline" in task):
            print(f"Project Name : {task['project_name']}")
            print(f"Deadline     : {task['deadline']}")

        print("-" * 40)


# ----------------------------
# Search Task
# ----------------------------
def search_task():

    tasks = load_tasks()

    task_id = input("Enter Task ID: ")

    for task in tasks:

        if task["task_id"] == task_id:

            print("\nTask Found!\n")

            print(f"Task ID      : {task['task_id']}")
            print(f"Title        : {task['title']}")
            print(f"Description  : {task['description']}")
            print(f"Assigned To  : {task['assigned_to']}")
            print(f"Priority     : {task['priority']}")
            print(f"Status       : {task['status']}")

            if task.get("type") == "project" or ("project_name" in task and "deadline" in task):
                print(f"Project Name : {task['project_name']}")
                print(f"Deadline     : {task['deadline']}")

            return

    print("Task Not Found!")


# ----------------------------
# Update Status
# ----------------------------
def update_status():

    tasks = load_tasks()

    task_id = input("Enter Task ID: ")

    for task in tasks:

        if task["task_id"] == task_id:

            print("\nCurrent Status:", task["status"])

            new_status = input(
                "Enter New Status (Pending/In Progress/Completed): "
            )

            if new_status not in [
                "Pending",
                "In Progress",
                "Completed"
            ]:
                print("Invalid Status!")
                return

            task["status"] = new_status

            save_tasks(tasks)

            print("Status Updated Successfully!")

            return

    print("Task Not Found!")


# ----------------------------
# Delete Task
# ----------------------------
def delete_task():

    tasks = load_tasks()

    task_id = input("Enter Task ID: ")

    for task in tasks:

        if task["task_id"] == task_id:

            tasks.remove(task)

            save_tasks(tasks)

            print("Task Deleted Successfully!")

            return

    print("Task Not Found!")


# ----------------------------
# View Completed Tasks
# ----------------------------
def completed_tasks():

    tasks = load_tasks()

    found = False

    print("\n====== COMPLETED TASKS ======\n")

    for task in tasks:

        if task["status"] == "Completed":

            found = True

            print(f"Task ID : {task['task_id']}")
            print(f"Title   : {task['title']}")
            print(f"Person  : {task['assigned_to']}")

            if task.get("type") == "project" or "project_name" in task:
                print(f"Project : {task['project_name']}")

            print("-" * 30)

    if not found:
        print("No Completed Tasks Found!")


# ----------------------------
# Highest Priority Task
# ----------------------------
def highest_priority_task():

    tasks = load_tasks()

    if not tasks:
        print("No Tasks Found!")
        return

    highest = max(tasks, key=lambda task: int(task["priority"]))

    print("\n====== HIGHEST PRIORITY TASK ======\n")

    print(f"Task ID      : {highest['task_id']}")
    print(f"Title        : {highest['title']}")
    print(f"Description  : {highest['description']}")
    print(f"Assigned To  : {highest['assigned_to']}")
    print(f"Priority     : {highest['priority']}")
    print(f"Status       : {highest['status']}")

    if highest.get("type") == "project" or ("project_name" in highest and "deadline" in highest):
        print(f"Project Name : {highest['project_name']}")
        print(f"Deadline     : {highest['deadline']}")


# ----------------------------
# Task Statistics Summary
# ----------------------------
def task_statistics():

    tasks = load_tasks()

    if not tasks:
        print("\nNo Tasks Found!")
        return

    total = len(tasks)
    pending = sum(1 for t in tasks if t.get("status") == "Pending")
    in_progress = sum(1 for t in tasks if t.get("status") == "In Progress")
    completed = sum(1 for t in tasks if t.get("status") == "Completed")
    project_tasks = sum(1 for t in tasks if t.get("type") == "project" or "project_name" in t)
    normal_tasks = total - project_tasks

    print("\n====== TASK STATISTICS ======\n")
    print(f"Total Tasks         : {total}")
    print(f"Normal Tasks        : {normal_tasks}")
    print(f"Project Tasks       : {project_tasks}")
    print(f"Pending Tasks       : {pending}")
    print(f"In Progress Tasks   : {in_progress}")
    print(f"Completed Tasks     : {completed}")
    print("=" * 30)