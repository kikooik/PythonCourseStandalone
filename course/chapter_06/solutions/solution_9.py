a = int(input())
b = int(input())

for i in range(1, a + 1):
    for j in range(i, a * b + 1, a):
        if j == (a * b):
            print(j)
        if j < 10:
            print(j, end="  ")
        elif j >= 10:
            print(j, end=" ")
    print()
    
 