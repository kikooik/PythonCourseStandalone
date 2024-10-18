n = int(input())
c = 0

for i in range(1, n + 1):
    p = n % i
    if p == 0:
        c += 1
        if c == 2:
            print(i)
            break