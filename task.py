class Task:

    # ----------------------------
    # Constructor
    # ----------------------------
    def __init__(self, task_id, title, description, assigned_to,
                 priority, status):

        self.task_id = task_id
        self.title = title
        self.description = description
        self.assigned_to = assigned_to

        # Encapsulated (Private)
        self.__priority = priority
        self.__status = status

    # ----------------------------
    # Getter for Priority
    # ----------------------------
    def get_priority(self):
        return self.__priority

    # ----------------------------
    # Setter for Priority
    # ----------------------------
    def set_priority(self, priority):

        if 1 <= priority <= 5:
            self.__priority = priority
        else:
            print("Priority must be between 1 and 5.")

    # ----------------------------
    # Getter for Status
    # ----------------------------
    def get_status(self):
        return self.__status

    # ----------------------------
    # Setter for Status
    # ----------------------------
    def set_status(self, status):

        allowed_status = ["Pending", "In Progress", "Completed"]

        if status in allowed_status:
            self.__status = status
        else:
            print("Invalid Status!")

    # ----------------------------
    # String Representation
    # ----------------------------
    def __str__(self):

        return (
            f"\nTask ID      : {self.task_id}\n"
            f"Title        : {self.title}\n"
            f"Description  : {self.description}\n"
            f"Assigned To  : {self.assigned_to}\n"
            f"Priority     : {self.__priority}\n"
            f"Status       : {self.__status}"
        )

    # ----------------------------
    # Official Representation
    # ----------------------------
    def __repr__(self):

        return (
            f"Task("
            f"{self.task_id}, "
            f"'{self.title}', "
            f"'{self.description}', "
            f"'{self.assigned_to}', "
            f"{self.__priority}, "
            f"'{self.__status}')"
        )

    # ----------------------------
    # Length of Task Title
    # ----------------------------
    def __len__(self):

        return len(self.title)

    # ----------------------------
    # Compare Task IDs
    # ----------------------------
    def __eq__(self, other):

        return self.task_id == other.task_id

    # ----------------------------
    # Compare Priority
    # ----------------------------
    def __gt__(self, other):

        if isinstance(other, Task):
            return self.__priority > other.get_priority()
        return False

    # ----------------------------
    # Convert Object to Dictionary
    # ----------------------------
    def to_dict(self):

        return {

            "task_id": self.task_id,
            "title": self.title,
            "description": self.description,
            "assigned_to": self.assigned_to,
            "priority": self.__priority,
            "status": self.__status,
            "type": "normal"

        }

    # ----------------------------
    # Display Task
    # ----------------------------
    def display(self):

        print(self)