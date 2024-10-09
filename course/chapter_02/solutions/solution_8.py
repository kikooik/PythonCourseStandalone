age = int(input())
i = str(input())
if (age < 0) or ((i != "N") and (i != "Y")):
    print("Введите корректные значения.")
elif (age >= 18) and (i == "Y"):
     print("Добро пожаловать в клуб!")
elif (age < 18) or (i == "N"):
    print("Извините, вход запрещен.")
