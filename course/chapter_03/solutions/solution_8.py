n = int(input())
n1 = 1
s = 0

while (n1 <= n):
    if n1 % 2 != 0:
        s = s + n1
    n1 += 1
print(s)