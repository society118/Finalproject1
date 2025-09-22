import json
from file_utils import load_tasks, save_tasks
from models import Task

file = "tasks.json"

def add_task():
    title = input("введите название задачи")
    new_task = {"title": title, "done": False}
    tasks = load_tasks()
    tasks.append(new_task)
    save_tasks(tasks)
    print("задача добавлена")


def del_task():
    tasks = load_tasks()
    if not tasks:
        print("список пуст")
        return
    for i, task in enumerate(tasks, start=1):
        print(i, ".", task.get("title", "без назви"))
    try:
        task_num = int(input("Введіть номер задачі для видалення: "))
    except ValueError:
        print("Помилка введено не число")
        return
    try:
        removed_task = tasks.pop(task_num - 1)
        save_tasks(tasks)
        print(f"Задача '{removed_task.get('title', 'без назви')}' удалена.")
    except IndexError:
        print("Неверный номер задачи")


def done_task():
    tasks = load_tasks()
    if not tasks:
        print("список пустий")
        return

    for i, task in enumerate(tasks, start=1):
        status = "прянято" if task.get("done") else "не принято"
        title = task.get("title", "без назви")
        print(f"{i}. {title} - {status}")

    try:
        task_num = int(input("Введите номер задачи для отметки как выполненной: "))
        tasks[task_num - 1]["done"] = True
        save_tasks(tasks)
        print("Задача отмечена как выполненная.")
    except ValueError:
        print("Ошибка: введено не число")
    except IndexError:
        print("Неверный номер задачи")



def list_task():
    tasks = load_tasks()
    if not tasks:
        print("список пуст")
        return
    for i, task in enumerate(tasks, start=1):
        if task.get("done"):
            status = "прянято"
        else:
            status = "не принято"
        try:
            title = task["title"]
        except KeyError:
            title = "без назви"
        print(f"{i}. {title} - {status}")


def show_menu():
    print("\n---------Menu---------")
    print("1.add  - добавляет")
    print("2.del  - удаляет")
    print("3.done - отметить задачу как выполненную")
    print("4.list - показать все задачи")
    print("5.exit - выход")
    print("\n---------Menu---------")

def main():
    while True:
        show_menu()
        choice = input("Введите команду: ").strip()

        if choice == "add":
            add_task()
        elif choice == "del":
            del_task()
        elif choice == "done":
            done_task()
        elif choice == "list":
            list_task()
        elif choice == "exit":
            print("Выход из программы")
            break
        else:
            print("Попробуйте ещё раз")


if __name__ == "__main__":
    main()
