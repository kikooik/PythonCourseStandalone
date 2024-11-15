n = int(input())
c = 0
s = 0

for i in range(1, n + 1):
    for j in range(1, i + 1):
        if (i % j) == 0:
            c += 1
            
    if c == 2:
        s += i
    c = 0
print(s)