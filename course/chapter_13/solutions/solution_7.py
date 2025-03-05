def apply_to_matrix(matrix, func):
    l = []
    for row in matrix:
        n_r = []
        for i in row:
            n_r.append(func(i))
        l.append(n_r)
    return l