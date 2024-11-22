a = int(input())

for i in range(a):
    for j in range(a):
        lay = min(i, j, a - i - 1, a - j - 1) + 1
        if (a - i - j - 1) == 0:
            print(lay, end="")
        else:
            print(lay, end=" ")
    print()    