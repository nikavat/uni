from table import *
rows = int(input("Введите количество строк: "))
column = int(input("Введите количество столбцов: "))
matrix = []
for i in range(rows):
    row = list(map(int, input(f"Введите элементы строки {i + 1} через пробел: ").split()))
    matrix.append(row)

print("Исходная таблица:")
for row in matrix:
    print(row)

print("Суммы строк: ", row_sums(matrix))
print("Суммы столбцов: ", column_sums(matrix))
print("Диагональный узор: ")
for row in diagonal_pattern(rows):
    print(row)
