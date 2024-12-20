start = (10.5, 22.7)
s = list(start)
x = float(input())
y = float(input())
now = (x, y)

if start == now:
    print("Вы находитесь в начальной точке маршрута")
else:
    print(round(start[0] - now[0], 1))
    print(round(start[1] - now[1], 1))
