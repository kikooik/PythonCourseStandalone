numbers = [3, 17, 6, 12, 9, 21, 5]
max = 0

for i in range(len(numbers)):
    if numbers[i] > max:
        max = numbers[i]
print("Максимальный элемент:", max)
