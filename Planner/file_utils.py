import json
file = "tasks.json"
def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
            return tasks
    except FileNotFoundError:
        return []


def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file,)

