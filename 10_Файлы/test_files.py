from pathlib import Path
from tempfile import TemporaryDirectory
from files_lab import read_matrix, selected_sum

with TemporaryDirectory() as directory:
    path = Path(directory) / "matrix.txt"

    path.write_text("1 2\n7 -1\n", encoding="utf-8")
    assert read_matrix(path) == [[7, -1]]

    path.write_text("1 1\n0\n", encoding="utf-8")
    assert read_matrix(path) == [[0]]

    # Проверка пустого файла
    path.write_text("", encoding="utf-8")

    try:
        read_matrix(path)
    except ValueError:
        pass
    else:
        assert False, "Пустой файл не обнаружен"

    # Проверка нулевого размера
    path.write_text("0 3\n", encoding="utf-8")

    try:
        read_matrix(path)
    except ValueError:
        pass
    else:
        assert False, "Нулевой размер не обнаружен"

    # Проверка неправильного количества элементов
    path.write_text("1 2\n1\n", encoding="utf-8")

    try:
        read_matrix(path)
    except ValueError as error:
        assert "Строка 2" in str(error)
    else:
        assert False, "Неверное количество элементов не обнаружено"

    # Проверка текста вместо числа
    path.write_text("1 2\n1 x\n", encoding="utf-8")

    try:
        read_matrix(path)
    except ValueError as error:
        assert "Строка 2" in str(error)
    else:
        assert False, "Нечисловое значение не обнаружено"

    # Проверка лишних строк
    path.write_text("1 1\n5\n7\n", encoding="utf-8")

    try:
        read_matrix(path)
    except ValueError:
        pass
    else:
        assert False, "Лишняя строка не обнаружена"

    # Проверка отсутствующего файла
    missing_path = Path(directory) / "missing.txt"

    try:
        read_matrix(missing_path)
    except FileNotFoundError:
        pass
    else:
        assert False, "Отсутствующий файл не обнаружен"

    # Проверка индивидуального варианта №2
    matrix = [
        [1, -2, 3],
        [4, 0, -6]
    ]

    assert selected_sum(matrix) == -8

    # Проверка отсутствия отрицательных чисел
    assert selected_sum([[1, 2], [3, 4]]) == 0

    print("Все проверки пройдены")