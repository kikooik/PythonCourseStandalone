g = int(input())
 
if (g >= 90) and (g <= 100):
    print("Отлично")
elif (g >= 75) and (g <= 89):
    print("Хорошо")
elif (g >= 50) and (g <= 74):
    print("Удовлетворительно")
elif (g < 50) and (g >= 0):
    print("Неудовлетворительно")
else:
    print("")