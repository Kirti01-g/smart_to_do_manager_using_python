import json
import os

FILE_PATH = "data/tasks.json"

def load_tasks():
    if not os.path.exists(FILE_PATH):
        return []
    with open(FILE_PATH, "r") as file:
        return json.load(file)

def save_tasks(tasks):
    with open(FILE_PATH, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task(title):
    tasks = load_tasks()
    tasks.append({"title": title, "completed": False})
    save_tasks(tasks)

def view_tasks():
    tasks = load_tasks()
    return tasks

def mark_complete(index):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        tasks[index]["completed"] = True
        save_tasks(tasks)

def delete_task(index):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        tasks.pop(index)
        save_tasks(tasks)
