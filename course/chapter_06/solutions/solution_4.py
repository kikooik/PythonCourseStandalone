n = int(input())

for i in range(n, 0, -1):
    for m in range(n, i - 1, -1):
        print(m, end='')
    print()