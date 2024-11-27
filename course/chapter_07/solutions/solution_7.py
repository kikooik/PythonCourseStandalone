numbers = [5, 10, 15, 20, 25, 30, 35, 40]
s = 0

for i in range(len(numbers)):
    s += numbers[i]
    
print("Среднее арифметическое:", s / len(numbers))