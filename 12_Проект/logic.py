def validate_records(records):
    """Проверяет записи, не изменяя их. При ошибке вызывает ValueError."""

    if not isinstance(records, list):
        raise ValueError("Данные должны быть списком")

    ids = set()

    for record in records:
        if not isinstance(record, dict):
            raise ValueError("Запись должна быть словарём")

        if type(record.get("id")) is not int or record["id"] <= 0:
            raise ValueError("Некорректный id")

        if not isinstance(record.get("title"), str) or record["title"].strip() == "":
            raise ValueError("Некорректное название")

        if not isinstance(record.get("category"), str) or record["category"].strip() == "":
            raise ValueError("Некорректная категория")

        if type(record.get("amount")) is not int or record["amount"] < 0:
            raise ValueError("Некорректное количество страниц")

        if type(record.get("completed")) is not bool:
            raise ValueError("Некорректный статус")

        if record["id"] in ids:
            raise ValueError("Повторяющийся id")

        ids.add(record["id"])


def add_record(records, title, category, amount):
    """Добавляет запись в список и возвращает новую запись."""

    if records == []:
        new_id = 1
    else:
        ids = []

        for record in records:
            ids.append(record["id"])

        new_id = max(ids) + 1

    new_record = {
        "id": new_id,
        "title": title.strip(),
        "category": category.strip(),
        "amount": amount,
        "completed": False
    }

    validate_records([new_record])

    records.append(new_record)

    return new_record


def find_records(records, query):
    """Возвращает найденные записи, не изменяя исходный список."""
    # records - список всех книг
    # query - поисковый запрос, то есть то, что пользователь хочет найти

    query = query.strip().lower()

    if query == "":
        raise ValueError("Поисковый запрос не должен быть пустым")

    found = []

    for record in records:
        if query in record["title"].lower():
        # Перебираем все книги и проверяем, содержится ли поисковый запрос внутри названия
            found.append(record)

    return found


def set_completed(records, record_id, completed):
    """Изменяет статус записи. Возвращает True при успехе, иначе False."""
    # record_id - ID книги, статус которой меняем
    # completed - новый статус прочтения

    if type(completed) is not bool:
        raise ValueError("Некорректный статус")

    for record in records:
        if record["id"] == record_id:
            record["completed"] = completed
            return True

    return False


def delete_record(records, record_id):
    """Удаляет запись по ID. Возвращает True при успехе, иначе False."""

    for i, record in enumerate(records):
        if record["id"] == record_id:
            records.pop(i)
            # Удаляет элемент по его индексу
            return True

    return False


def statistics(records):
    """Возвращает статистику, не изменяя исходный список."""

    total = len(records)
    # Общее количество книг
    completed = 0
    # Количество прочитанных книг
    total_amount = 0
    # Общее количество страниц
    categories = {}
    # Суммы страниц по жанрам

    for record in records:
        if record["completed"]:
            completed += 1

        total_amount += record["amount"]

        category = record["category"].strip()

        if category not in categories:
            categories[category] = 0

        categories[category] += record["amount"]

    return {
        "total": total,
        "completed": completed,
        "unfinished": total - completed,
        "total_amount": total_amount,
        "categories": dict(sorted(categories.items()))
    }