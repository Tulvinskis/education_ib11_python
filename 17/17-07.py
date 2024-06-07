def transpose(matrix):
    n = len(matrix)
    m = len(matrix[0])
    for j in range(m):
        transpose_matrix = []
        for i in range(n):
            transpose_matrix = transpose_matrix + [matrix[i][j]]
        matrix = matrix + [transpose_matrix]
    return matrix


matrix = [[1]]
transpose(matrix)
for line in matrix:
    print(*line)