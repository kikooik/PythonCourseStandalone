n = int(input())

for i in range(1, n + 1):
    for m in range(n, i - 1, -1):
        print(m, end='')
    print()