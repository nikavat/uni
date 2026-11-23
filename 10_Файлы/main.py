def read_positive_integer():
    while True:
        try:
            number = int(input("Введите целое положительное число: "))
        except ValueError:
            print("Не целое число")
        else:
            if number > 0:
                return number
            else: print("Должно быть больше нуля")

from pathlib import Path
from files_lab import *
from table import *

folder = Path(__file__).resolve().parent

matrix_path = folder / 'matrix.txt'
report_path = folder / 'report.txt'

try:
    matrix = read_matrix(matrix_path)
    row_result = row_sums(matrix)
    column_result = column_sums(matrix)
    variant_result = selected_sum(matrix)
    with open(report_path, "w", encoding="utf-8") as file:
        file.write("Суммы строк: " + " ".join(map(str, row_result)) + "\n")
        file.write("Суммы столбцов: " + " ".join(map(str, column_result)) + "\n")
        file.write(f"Результат варианта: {variant_result}\n")
    print("Отчёт успешно создан")

except FileNotFoundError:
    print("Файл не найден")

except UnicodeError:
    print("Ошибка кодировки файла")

except ValueError as error:
    print("Ошибка формата:", error)

except OSError as error:
    print("Ошибка работы с файлом:", error)