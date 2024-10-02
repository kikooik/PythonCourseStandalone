age = int(input())
i = str(input())
 
if (age >= 18) or (i == "Y"):
     print("Добро пожаловать в клуб!")
elif (age < 18) and (i == "N"):
    print("Извините, вход запрещен.")
else:
    print("Введите корректные значения.")