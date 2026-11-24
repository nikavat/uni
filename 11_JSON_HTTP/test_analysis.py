import json
from pathlib import Path
from tempfile import TemporaryDirectory
from analysis import *

folder = Path(__file__).resolve().parent

with open(folder / "todos.json", "r", encoding="utf-8") as file:
    todos = json.load(file)

validate_todos(todos)

counts = completion_counts(todos)
leaders = top_users(counts)

assert counts == {5: 2, 10: 2}
assert leaders == [5, 10]

selected = []

for todo in todos:
    if todo["userId"] in leaders and todo["completed"]:
        selected.append(todo)

ids = []

for todo in selected:
    ids.append(todo["id"])

assert ids == [1, 3, 4, 5]

assert completion_counts([]) == {}
assert top_users({}) == []
assert select_tasks([], 5) == []

unfinished = [
    {"id": 1, "userId": 5, "title": "Ввод", "completed": False},
    {"id": 2, "userId": 10, "title": "Циклы", "completed": False}
]

assert completion_counts(unfinished) == {5: 0, 10: 0}
assert top_users(completion_counts(unfinished)) == []
assert select_tasks(unfinished, 5) == []

assert top_users({5: 3, 10: 1}) == [5]
assert top_users({10: 2, 5: 2}) == [5, 10]


ids = []

for todo in select_tasks(todos, 5):
    ids.append(todo["id"])

assert ids == [1, 5]
assert select_tasks(todos, 99) == []
assert select_tasks(unfinished, 5) == []

def check_invalid(data):
    try:
        validate_todos(data)
        # Пытаемся проверить переданные данные
    except ValueError:
    # Если возникла ожидаемая ошибка, тест пройден
        pass
        # Ничего не делаем
    else:
        assert False, "Ожидалась ошибка ValueError"
        # Намеренно проваливаем тест, поскольку неправильные данные не должны проходить проверку

check_invalid({})

check_invalid([
    {"id": 1, "userId": 5, "title": "Ввод", "completed": True},
    {"id": 1, "userId": 10, "title": "Циклы", "completed": False}
])

check_invalid([
    {"id": 1, "title": "Ввод", "completed": True}
])

check_invalid([
    {"id": 1, "userId": 5, "title": "Ввод", "completed": "false"}
])

check_invalid([
    {"id": True, "userId": 5, "title": "Ввод", "completed": True}
])

with TemporaryDirectory() as directory:
    path = Path(directory) / "test.json"

    with open(path, "w", encoding="utf-8") as file:
        json.dump(selected, file, ensure_ascii=False, indent=2)

    with open(path, "r", encoding="utf-8") as file:
        restored = json.load(file)

    assert restored == selected

print("Все проверки пройдены")