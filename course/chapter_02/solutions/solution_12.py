a = int(input())
b = int(input())
c = int(input())

if (c < a + b) and (a < b + c) and (b < a + c):
    print("Такой треугольник существует")
else:
    print("Такой треугольник не существует")