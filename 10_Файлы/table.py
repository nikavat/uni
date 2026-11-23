def row_sums(matrix):
    result = []
    for row in matrix:
        result.append(sum(row))
    return result

def column_sums(matrix):
    result = []
    if not matrix:
        return []
    for column in range(len(matrix[0])):
        sum = 0
        for row in matrix:
            sum += row[column]
        result.append(sum)
    return result

def diagonal_pattern(size):
    matrix = []
    for row in range(size):
        current_row = []
        for column in range(size):
            if row == column:
                current_row.append(0)
            elif row < column:
                current_row.append(1)
            else: current_row.append(2)
        matrix.append(current_row)
    return matrix

def transform(matrix):
    result = []
    for row in matrix:
        current_row = []
        for number in row:
            if number > 0:
                current_row.append(1)
            else: current_row.append(number)
        result.append(current_row)
    return result