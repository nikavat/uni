import json
from logic import validate_records


def load_records(path):
    """Загружает и проверяет список записей."""

    with open(path, "r", encoding="utf-8") as file:
        records = json.load(file)
        # Открываем файл в режиме чтения и преобразуем содержимое JSON в список словарей Python.

    validate_records(records)
    # Проверяем загруженные данные нашей функцией из logic.py.

    return records
    # Возвращаем проверенный список книг.


def save_records(path, records):
    """Проверяет и сохраняет список записей."""

    validate_records(records)
    # Перед записью дополнительно проверяем корректность данных.

    with open(path, "w", encoding="utf-8") as file:
        json.dump(records, file, ensure_ascii=False, indent=4)
        # "w" - режим записи с перезаписью содержимого;
        # encoding="utf-8" - кодировка;
        # ensure_ascii=False - сохранение русских букв в читаемом виде;
        # indent=4 - отступы для красивого оформления JSON.