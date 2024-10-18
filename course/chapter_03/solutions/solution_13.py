password = "w1w2w3w4"
c = 0

while (c != 3):
    p = input()
    c += 1
    if (p == password):
        print("Доступ разрешён.")
        break
    elif (c == 3):
        print("Доступ запрещен")
        break
    elif (p != password):
        print("Неверный пароль, попробуйте снова.")
    
    
    