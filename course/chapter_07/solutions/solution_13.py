numbers = [int(i) for i in input().split()]

n = int(input())
s = 0

for i in numbers[-n:]:
    s += i
    
print(s)