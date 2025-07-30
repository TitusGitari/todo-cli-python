import json
import os

TASKS_FILE = "tasks.json"

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, 'r') as f:
        return json.load(f)

def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as f:
        json.dump(tasks, f, indent=4)

import argparse

parser = argparse.ArgumentParser(description="Simple CLI To-Do App")
parser.add_argument("command", choices=["add", "list", "remove", "done"], help="Command to run")
parser.add_argument("--task", help="Task description")
parser.add_argument("--index", type=int, help="Task index to remove or mark done")

args = parser.parse_args()

tasks = load_tasks()

if args.command == "add" and args.task:
    tasks.append({"task": args.task, "done": False})
    save_tasks(tasks)
    print(f"Added task: {args.task}")

elif args.command == "list":
    if not tasks:
        print("No tasks found.")
    for i, task in enumerate(tasks):
        status = "✅" if task["done"] else "❌"
        print(f"{i}. {task['task']} [{status}]")

elif args.command == "remove" and args.index is not None:
    if 0 <= args.index < len(tasks):
        removed = tasks.pop(args.index)
        save_tasks(tasks)
        print(f"Removed task: {removed['task']}")
    else:
        print("Invalid index.")

elif args.command == "done" and args.index is not None:
    if 0 <= args.index < len(tasks):
        tasks[args.index]["done"] = True
        save_tasks(tasks)
        print(f"Marked task as done: {tasks[args.index]['task']}")
    else:
        print("Invalid index.")
else:
    print("Invalid usage. Use --help for options.")

