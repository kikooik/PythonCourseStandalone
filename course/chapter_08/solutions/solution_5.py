from copy import deepcopy


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

new_matrix=deepcopy(matrix)

for i in range(3):
    for j in range(3):
        new_matrix[i][j] = matrix[j][i]
    
for i in range(3):
    for j in range(3):
        if j == 2:
            print(new_matrix[i][j], end="")
        else:
            print(new_matrix[i][j], end=" ")
    print()