from menu import display_menu
from task_manager import (
    add_task,
    view_tasks,
    search_task,
    update_status,
    delete_task,
    completed_tasks,
    highest_priority_task,
)


def main():
    while True:

        display_menu()

        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_task()

        elif choice == "2":
            view_tasks()

        elif choice == "3":
            search_task()

        elif choice == "4":
            update_status()

        elif choice == "5":
            delete_task()

        elif choice == "6":
            completed_tasks()

        elif choice == "7":
            highest_priority_task()

        elif choice == "8":
            print("\nThank you for using Task Manager!")
            break

        else:
            print("\nInvalid choice! Please try again.")


if __name__ == "__main__":
    main()