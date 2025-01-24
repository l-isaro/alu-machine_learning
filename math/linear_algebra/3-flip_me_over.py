def matrix_transpose(matrix):
    transpose = []
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            transpose[j][i] = matrix[i][j] 
    return transpose

print(matrix_transpose([[1, 2], [3, 4]]))
