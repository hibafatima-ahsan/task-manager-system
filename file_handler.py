import json

FILE_NAME = "tasks.json"


# ----------------------------
# Load Tasks
# ----------------------------
def load_tasks():

    try:
        with open(FILE_NAME, "r") as file:

            data = json.load(file)

            return data

    except FileNotFoundError:

        return []

    except json.JSONDecodeError:

        return []


# ----------------------------
# Save Tasks
# ----------------------------
def save_tasks(tasks):

    with open(FILE_NAME, "w") as file:

        json.dump(tasks, file, indent=4)