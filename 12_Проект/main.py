import json
from pathlib import Path
from logic import *
from storage import *

def read_text(prompt):
# prompt - текст приглашения к вводу
    while True:
        text = input(prompt).strip()
        # Получаем строку от пользователя и убираем пробелы по краям.

        if text == "":
            print("Строка не должна быть пустой")
        else:
            return text
        # Если строка пустая, цикл начинается заново. Если нет - возвращаем строку и завершаем функцию.

def read_integer(prompt, minimum):
# minimum - минимальное допустимое значение
    while True:
        try:
            number = int(input(prompt))

            if number < minimum:
                print(f"Число должно быть не меньше {minimum}")
            else:
                return number

        except ValueError:
            print("Введите целое число")

def get_id(record):
    return record["id"]
# Возвращает ID записи для сортировки.

def show_records(records):
    if records == []:
        print("Нет записей")
        return
    # Проверка пустого списка

    for record in sorted(records, key=get_id):
    # Сортировка по ID
    # Python самостоятельно вызывает get_id() для каждой записи, получает её ID и сортирует книги по этим значениям.
        if record["completed"]:
            status = "Прочитано"
        else:
            status = "Не прочитано"
        # Преобразование статуса

        print(f'{record["id"]}. {record["title"]} | '
              f'{record["category"]} | {record["amount"]} стр. | '
              f'{status}')

def show_statistics(records):
    """Выводит статистику списка книг."""

    stats = statistics(records)
    # Получаем статистику.

    print("Всего книг:", stats["total"])
    print("Прочитано:", stats["completed"])
    print("Не прочитано:", stats["unfinished"])
    print("Всего страниц:", stats["total_amount"])

    print("Количество страниц по жанрам:")

    for category, amount in stats["categories"].items():
        print(f"{category}: {amount} стр.")

def show_menu():
    """Выводит главное меню программы."""

    print("\nСписок книг для чтения")
    # \n - символ переноса строки
    print("1. Показать книги")
    print("2. Добавить книгу")
    print("3. Найти книгу")
    print("4. Изменить статус книги")
    print("5. Удалить книгу")
    print("6. Показать статистику")
    print("7. Сохранить данные")
    print("8. Выйти")

def main():
    """Запускает основную программу."""

    path = Path(__file__).resolve().parent / "data.json"
    # Формируем путь к файлу.

    try:
        records = load_records(path)
        # Функция из storage.py открывает JSON-файл, проверяет его содержимое и возвращает список книг.

    except FileNotFoundError:
        print("Файл не найден. Создан пустой список")
        records = []
        # Обрабатываем отсутствие файла.

    except json.JSONDecodeError:
        print("Некорректный JSON")
        return

    except UnicodeError:
        print("Ошибка кодировки файла")
        return

    except ValueError as error:
        print("Ошибка структуры данных:", error)
        return

    except OSError as error:
        print("Ошибка доступа к файлу:", error)
        return

    while True:
        show_menu()
        choice = input("Выберите действие: ").strip()
        # Получение команды.

        if choice == "1":
            show_records(records)

        elif choice == "2":
            title = read_text("Введите название книги: ")
            category = read_text("Введите жанр: ")
            amount = read_integer("Введите количество страниц: ", 0)

            add_record(records, title, category, amount)
            print("Книга успешно добавлена")
        # Добавление книги

        elif choice == "3":
            query = read_text("Введите название для поиска: ")
            found = find_records(records, query)

            if found == []:
                print("Книги не найдены")
            else:
                show_records(found)
        # Поиск книги.
        # found - список словарей с найденными книгами

        elif choice == "4":
            record_id = read_integer("Введите ID книги: ", 1)

            while True:
                status = input("Книга прочитана? (да/нет): ").strip().lower()
                # Получаем ответ пользователя, убираем лишние пробелы и переводим строку в нижний регистр.

                if status == "да":
                    completed = True
                    break

                elif status == "нет":
                    completed = False
                    break
                # Преобразуем текстовый ответ в логическое значение.

                else:
                    print("Введите да или нет")

            if set_completed(records, record_id, completed):
                print("Статус успешно изменён")

            else:
                print("Книга с таким ID не найдена")

        elif choice == "5":
            record_id = read_integer("Введите ID книги: ", 1)

            confirmation = input("Удалить книгу? (да/нет): ").strip().lower()
            # confirmation - подтверждение

            if confirmation == "да":
                if delete_record(records, record_id):
                    print("Книга успешно удалена")
                else:
                    print("Книга с таким ID не найдена")
            else:
                print("Удаление отменено")

        elif choice == "6":
            show_statistics(records)

        elif choice == "7":
            try:
                save_records(path, records)
                # Передаём путь к нашему data.json и текущий список книг в функцию из storage.py.
                print("Данные успешно сохранены")

            except (OSError, ValueError) as error:
                print("Ошибка сохранения:", error)

        elif choice == "8":
            while True:
                answer = input("Сохранить данные перед выходом? (да/нет): ").strip().lower()

                if answer == "да" or answer == "нет":
                    break
                # Если пользователь ввёл один из двух допустимых ответов, завершаем внутренний цикл ввода.

                print("Введите да или нет")

            if answer == "да":
            # Если пользователь согласился сохранить данные, выполняем сохранение. Если ответил «нет», пропускаем этот блок.
                try:
                    save_records(path, records)
                    print("Данные успешно сохранены")

                except (OSError, ValueError) as error:
                    print("Ошибка сохранения:", error)
                    continue
                # Если при сохранении возникла ошибка, continue возвращает нас к началу главного цикла, то есть снова показывает меню.

            print("Программа завершена")
            break

        else:
            print("Некорректная команда")

if __name__ == "__main__":
    main()