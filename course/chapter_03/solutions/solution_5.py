password = "12345678"
p1 = 0

while (password != p1):
    p1 = input()
    if (password == p1):
        print("Доступ разрешён.")
    else:
        print("Неверный пароль, попробуйте снова.")