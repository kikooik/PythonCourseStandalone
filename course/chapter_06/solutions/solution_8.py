n = int(input())
s = ""

for _ in range(n):
    n1 = input()
    s += n1
    
s = int(s)
j = 0
n1 = 1
while s != 0:
    n1 = s % 10
    j = j + n1
    s = s // 10
print(j)