a = int(input())
b = int(input())

m = len(str(a * b))

for i in range(1, a + 1):
    for j in range(i, a * b + 1, a):
        t = len(str(j))
        p = (m - t) + 1
        if (a * b - j) < a:
            print(j, end="")
        else:
            print(j, end=(" " * p))
    print()