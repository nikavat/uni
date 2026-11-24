def validate_todos(data):
    if not isinstance(data, list):
        raise ValueError("Данные должны быть списком")

    ids = set()

    for todo in data:
        if not isinstance(todo, dict):
            raise ValueError("Задача должна быть словарём")

        if type(todo.get("id")) is not int or todo["id"] <= 0:
            raise ValueError("Некорректный id")

        if type(todo.get("userId")) is not int or todo["userId"] <= 0:
            raise ValueError("Некорректный userId")

        if not isinstance(todo.get("title"), str) or todo["title"].strip() == "":
            raise ValueError("Некорректное название задачи")

        if type(todo.get("completed")) is not bool:
            raise ValueError("Некорректное значение completed")

        if todo["id"] in ids:
            raise ValueError("Повторяющийся id")

        ids.add(todo["id"])


def completion_counts(todos):
    counts = {}

    for todo in todos:
        user_id = todo["userId"]

        if user_id not in counts:
            counts[user_id] = 0

        if todo["completed"]:
            counts[user_id] += 1

    return counts

def top_users(counts):
    if not counts:
        return []

    maximum = max(counts.values())
    if maximum == 0:
        return []
    leaders = []

    for users_id in counts:
        if counts[users_id] == maximum:
            leaders.append(users_id)

    return sorted(leaders)


def select_tasks(todos, user_id, parameter=None):
    selected = []

    for todo in todos:
        if todo["userId"] == user_id and todo["completed"]:
            selected.append(todo)

    return selected