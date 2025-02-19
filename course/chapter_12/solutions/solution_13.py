def replace_in_matrix(matrix, old_value, new_value):
    for i in range(len(matrix)):
        if old_value in matrix[i]:
            for n in range(len(matrix[i])):
                if matrix[i][n] == old_value:
                    matrix[i][n] = new_value
    return matrix   

matrix = [[1, 2, 3], [1, 2, 1], [3, 1, 2]]
replace_in_matrix(matrix, 1, 9)
print(matrix)