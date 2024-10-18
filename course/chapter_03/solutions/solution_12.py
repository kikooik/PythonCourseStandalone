num = 25
c = 0

while (c != 5):
    n = int(input())
    c += 1
    if (n == num):
        print("Поздравляем! Вы угадали число.")
        break
    elif (n < num):
        print("Загаданное число больше.")
    elif (n > num):
        print("Загаданное число меньше.")
    if (c == 5):
        print("Попытки закончились")
        break