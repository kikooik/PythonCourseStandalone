c = 0
s = 0

while (c != 5):
    a = int(input())
    if (a < 0):
        continue
    else:
        c += 1
        s += a
print(s)