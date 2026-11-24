import json
from pathlib import Path
from analysis import *

folder = Path(__file__).resolve().parent

todos_path = folder / "todos.json"
leaders_path = folder / "leaders.json"
selected_path = folder / "selected.json"

def read_user_id():
    while True:
        try:
            user_id = int(input("Введите ID пользователя: "))

            if user_id <= 0:
                print("ID должен быть положительным")
                continue

            return user_id

        except ValueError:
            print("Введите целое число: ")

try:
    with open(todos_path, "r", encoding="utf-8") as file:
        todos = json.load(file)
        # json.load() - читаем JSON из файла

    validate_todos(todos)

    counts = completion_counts(todos)
    leaders = top_users(counts)

    selected = []

    for todo in todos:
        if todo["userId"] in leaders and todo["completed"]:
            selected.append(todo)

    print("Количество выполненных задач:", counts)
    print("Лидеры:", leaders)

    with open(leaders_path, "w", encoding="utf-8") as file:
        json.dump(selected, file, ensure_ascii=False, indent=4)
        # json.dump() - записываем JSON в файл
        # selected - список задач, который записываем
        # file - файл, в который записываем данные
        # ensure_ascii=False - сохраняет русские буквы в читаемом виде
        # indent=4 - форматирует JSON с отступами в четыре пробела

    print("Результаты успешно сохранены")

    user_id = read_user_id()

    selected = select_tasks(todos, user_id)

    with open(selected_path, "w", encoding="utf-8") as file:
        json.dump(selected, file, ensure_ascii=False, indent=4)

    print("Выбранные задачи сохранены")

except FileNotFoundError:
    print("Файл не найден")

except UnicodeError:
    print("Ошибка кодировки файла")

except json.JSONDecodeError as error:
    print("Некорректный JSON:", error)

except ValueError as error:
    print("Ошибка структуры данных:", error)

except OSError as error:
    print("Ошибка доступа к файлу:", error)