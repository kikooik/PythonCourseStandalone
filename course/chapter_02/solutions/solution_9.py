n = int(input())
n1 = int(input())

x = ((n >= 10) and (n <= 20)) or ((n >= 50) and (n <= 60))
y = ((n1 >= 10) and (n1 <= 20)) or ((n1 >= 50) and (n1 <= 60))

if (x == True) and (y == True):
    print("Числа в диапазоне.")
else: 
    print("Числа вне диапазона.")