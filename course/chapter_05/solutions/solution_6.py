n = int(input())
s = "!"
l = ""

for i in range(1, n + 1):
    if i != n:
        print(s * i, end="_")
    else:
        print(s * i)
        
        
