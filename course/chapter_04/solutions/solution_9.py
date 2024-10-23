n = int(input())
n1 = int(input())
x = int(input())
s = 0
print(n)
print(n1)

for _ in range(x - 2):
    s = n + n1
    n = n1
    n1 = s
    print(s)