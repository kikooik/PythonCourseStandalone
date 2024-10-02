t = int(input())

if (t >= 6) and (t <= 11):
    print("Доброе утро!")
elif (t >= 12) and (t <= 17):
    print("Добрый день!")
elif (t >= 18) and (t <= 21):
    print("Добрый вечер!")
elif (t <= 5) and (t >= 0) or ((t >= 22) and (t <= 23)):
    print("Доброй ночи!")
