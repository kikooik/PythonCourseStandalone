def even_numbers(n):
    g = (i for i in range(1, n + 1) if i % 2 == 0)
    return g