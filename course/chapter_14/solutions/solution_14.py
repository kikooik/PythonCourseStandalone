def fibonacci(n):
    f1, f2 = 1, 1
    for _ in range(n):
        yield f1
        f1, f2 = f2, f1 + f2
        