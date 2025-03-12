def factorials(n):
    p = 1
    for i in range(1, n + 1):
        p *= i
        yield p
