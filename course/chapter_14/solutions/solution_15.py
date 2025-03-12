def multiples_of_3_or_5(n):
    g = (i for i in range(1, n + 1) if i % 3 == 0 or i % 5 == 0)
    return g