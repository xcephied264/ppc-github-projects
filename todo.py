import argparse
import json
from pathlib import Path


def load_tasks(file_path="tasks.json"):
    path = Path(file_path)
    if not path.exists():
        return []
    return json.loads(path.read_text(encoding="utf-8"))


def save_tasks(tasks, file_path="tasks.json"):
    Path(file_path).write_text(
        json.dumps(tasks, indent=2),
        encoding="utf-8"
    )


def add_task(title, file_path="tasks.json"):
    tasks = load_tasks(file_path)
    next_id = max((task["id"] for task in tasks), default=0) + 1

    task = {
        "id": next_id,
        "title": title,
        "done": False
    }

    tasks.append(task)
    save_tasks(tasks, file_path)
    return task


def complete_task(task_id, file_path="tasks.json"):
    tasks = load_tasks(file_path)

    for task in tasks:
        if task["id"] == task_id:
            task["done"] = True
            save_tasks(tasks, file_path)
            return True

    return False


def main():
    parser = argparse.ArgumentParser(description="Python To-Do App")
    parser.add_argument("--file", default="tasks.json")

    commands = parser.add_subparsers(dest="command", required=True)

    add = commands.add_parser("add")
    add.add_argument("title")

    commands.add_parser("list")

    done = commands.add_parser("done")
    done.add_argument("id", type=int)

    args = parser.parse_args()

    if args.command == "add":
        task = add_task(args.title, args.file)
        print(f"Added task #{task['id']}: {task['title']}")

    elif args.command == "list":
        for task in load_tasks(args.file):
            status = "Done" if task["done"] else "Todo"
            print(f"{task['id']}. [{status}] {task['title']}")

    elif args.command == "done":
        if complete_task(args.id, args.file):
            print(f"Completed task #{args.id}")
        else:
            print("Task not found")


if __name__ == "__main__":
    main()