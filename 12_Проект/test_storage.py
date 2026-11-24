from pathlib import Path
from tempfile import TemporaryDirectory
from storage import *
from logic import *

def test_save_load():
    records = []

    add_record(records, "Пси", "Триллер", 320)
    add_record(records, "Тени Сентфора", "Детектив", 250)

    set_completed(records, 1, True)

    with TemporaryDirectory() as folder:
    # Создаём временную папку, которая автоматически удалится после выхода из блока with.
        path = Path(folder) / "data.json"
        # Формируем путь к файлу внутри временной папки.

        save_records(path, records)
        # Сохраняем список книг в этот файл.

        loaded = load_records(path)
        # Загружаем данные обратно в Python и записываем их в переменную loaded.

        assert loaded == records
        # Сравниваем загруженные данные с исходными. Если хотя бы одно поле изменилось, возникнет ошибка AssertionError.

def test_empty():
    with TemporaryDirectory() as folder:
        path = Path(folder) / "data.json"

        save_records(path, [])
        # Передаём в функцию save_records() два аргумента: path - куда сохранять; [ ] - что сохранять (пустой список).

        assert load_records(path) == []
        # Загружаем содержимое файла и сравниваем его с пустым списком.

if __name__ == "__main__":
    test_save_load()
    test_empty()

    print("Все тесты успешно пройдены")