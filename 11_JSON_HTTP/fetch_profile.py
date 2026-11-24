import json
# Работа с JSON
import socket
# Обработка ошибок ожидания сетевого ответа
from pathlib import Path
# Работа с путями к файлам
from urllib.error import HTTPError, URLError
# Обработка ошибок HTTP; Обработка ошибок сетевого запроса
from urllib.parse import quote
# Кодирование специальных символов в URL
from urllib.request import Request, urlopen
# Формирование HTTP-запроса; Отправка запроса и получение ответа


def fetch_profile(login):
    if login.strip() == "":
        raise ValueError("Логин не должен быть пустым")
    url = "https://api.github.com/users/" + quote(login.strip(), safe="")
    request = Request(url, headers={
    # Request() - создаёт объект HTTP-запроса
    # Headers - словарь заголовков запроса
        "Accept": "application/vnd.github+json",
        # Accept - сообщает серверу, в каком формате хотим получить данные (JSON)
        "User-Agent": "python-course-lab11",
        # User-Agent - сообщает серверу, какая программа отправляет запрос
    })
    with urlopen(request, timeout=10) as response:
        data = json.loads(response.read().decode("utf-8"))
        # response.read() - cчитывает полученные от сервера данные в виде байтов
        # .decode("utf-8") - преобразуем байты в строку
        # json.loads(...) - преобразуем полученную строку в объект Python
    if not isinstance(data, dict) or not isinstance(data.get("login"), str):
        raise ValueError("Ответ не похож на профиль пользователя")
    return data


def main():
    try:
        data = fetch_profile(input("Логин GitHub: "))
        output = Path(__file__).resolve().parent / "profile.json"
        with open(output, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=2)
            # Записываем полученный словарь в JSON-файл
        print(f"Профиль сохранён: {data['login']}")
    except HTTPError as error:
        print(f"Сервер вернул HTTP {error.code}")
    except (URLError, TimeoutError, socket.timeout):
        print("Не удалось получить ответ по сети")
    except (ValueError, UnicodeError) as error:
        print(f"Ошибка данных: {error}")
    except OSError as error:
        print(f"Ошибка доступа: {error}")


if __name__ == "__main__":
    main()
# Позволяет запускать функцию main() только при непосредственном запуске файла fetch_profile.py, а не при его импорте в другой модуль