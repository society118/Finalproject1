class Task:
    def __init__(self, id: int, title: str, deadline: str, done: bool = False):
        self.id = id
        self.title = title
        self.deadline = deadline
        self.done = done

menu = """Menu:

add  - добавляет
del  - удаляет
done - отметить задачу как выполненную
list - показать все задачи
exit - выход
"""