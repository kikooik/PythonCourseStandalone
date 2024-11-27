numbers = [12, -7, 5, -3, 8, -2]

for i in range(len(numbers)):
    if numbers[i] < 0:
        numbers[i] = 0
        
print("Список после замены:", numbers)