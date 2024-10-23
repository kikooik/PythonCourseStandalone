n = 1
n1 = 1
print("Числа Фибоначчи:")
print(n)
print(n1)
for _ in range(8):
    f = n + n1
    n = n1
    n1 = f
    print(f)
