def read_matrix(path):
    with open(path, "r", encoding="utf-8") as file:
        lines = file.read().splitlines()

    if not lines:
        raise ValueError("Файл пустой")

    try:
        rows, columns = map(int, lines[0].split())
    except ValueError:
        raise ValueError("Строка 1: неверный заголовок")

    if rows <= 0 or columns <= 0:
        raise ValueError("Строка 1: размеры должны быть положительными")

    if len(lines) != rows + 1:
        raise ValueError("Неверное количество строк")

    matrix = []

    for i in range(1, len(lines)):
        try:
            row = list(map(int, lines[i].split()))
        except ValueError:
            raise ValueError(f"Строка {i + 1}: обнаружено не целое число")

        if len(row) != columns:
            raise ValueError(f"Строка {i + 1}: неверное количество элементов")

        matrix.append(row)
    return matrix

def selected_sum(matrix):
    total = 0
    for row in matrix:
        for number in row:
            if number < 0:
                total += number
    return total