from task import Task


class ProjectTask(Task):

    # ----------------------------
    # Constructor
    # ----------------------------
    def __init__(
        self,
        task_id,
        title,
        description,
        assigned_to,
        priority,
        status,
        deadline,
        project_name
    ):

        # Call Parent Constructor
        super().__init__(
            task_id,
            title,
            description,
            assigned_to,
            priority,
            status
        )

        # New attributes
        self.deadline = deadline
        self.project_name = project_name

    # ----------------------------
    # Display Project Task
    # ----------------------------
    def display(self):

        print("\n========== Project Task ==========")
        super().display()
        print(f"Project Name : {self.project_name}")
        print(f"Deadline     : {self.deadline}")

    # ----------------------------
    # Convert Object to Dictionary
    # ----------------------------
    def to_dict(self):

        data = super().to_dict()

        data["project_name"] = self.project_name
        data["deadline"] = self.deadline
        data["type"] = "project"

        return data

    # ----------------------------
    # String Representation
    # ----------------------------
    def __str__(self):

        return (
            super().__str__()
            + f"\nProject Name : {self.project_name}"
            + f"\nDeadline     : {self.deadline}"
        )

    # ----------------------------
    # Official Representation
    # ----------------------------
    def __repr__(self):

        return (
            f"ProjectTask("
            f"{self.task_id}, "
            f"'{self.title}', "
            f"'{self.description}', "
            f"'{self.assigned_to}', "
            f"{self.get_priority()}, "
            f"'{self.get_status()}', "
            f"'{self.deadline}', "
            f"'{self.project_name}')"
        )