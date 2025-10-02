def transpose_matrix(matrix):
    if not matrix or not matrix[0]:
        return []

    rows = 0
    for row in matrix:
        rows += 1
    cols = 0
    if rows > 0:
        for element in matrix[0]:
            cols += 1

    transposed = []
    i = 0
    while i < cols:
        new_row = []
        j = 0
        while j < rows:
            new_row.append(matrix[j][i])
            j += 1
        transposed.append(new_row)
        i += 1

    return transposed


matrix_a = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix_b = [
    [10, 20],
    [30, 40],
    [50, 60]
]

print(f"Исходная матрица A: {matrix_a}")
transposed_a = transpose_matrix(matrix_a)
print(f"Транспонированная A: {transposed_a}")

print(f"\nИсходная матрица B: {matrix_b}")
transposed_b = transpose_matrix(matrix_b)
print(f"Транспонированная B: {transposed_b}")
