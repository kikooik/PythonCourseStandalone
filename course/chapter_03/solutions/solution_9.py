n = int(input())
s = 0
n1 = 1
while n != 0:
    n1 = n % 10
    s = s + n1
    n = n // 10
print(s)