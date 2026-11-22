from table import *

assert row_sums([[1, 2, 3], [4, 5, 6]]) == [6, 15]
assert column_sums([[1, 2, 3], [4, 5, 6]]) == [5, 7, 9]

assert row_sums([[7]]) == [7]
assert column_sums([[7]]) == [7]
assert diagonal_pattern(1) == [[0]]


assert row_sums([[1], [-1], [0]]) == [1, -1, 0]
assert column_sums([[1], [-1], [0]]) == [0]

assert row_sums([]) == []
assert column_sums([]) == []
assert transform([]) == []

assert diagonal_pattern(3) == [
    [0, 1, 1],
    [2, 0, 1],
    [2, 2, 0]
]

matrix = [
    [-2, 0, 3],
    [4, -5, 6]
]
result = transform(matrix)
assert result == [
    [-2, 0, 1],
    [1, -5, 1]
]

print("Все проверки пройдены")