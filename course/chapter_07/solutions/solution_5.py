numbers = [4, 7, 2, 9, 8, 5, 6, 3, 0, 1]
l = list()

for i in range(len(numbers)):
    if numbers[i] % 2 == 0:
        l.append(i)
print(*l, sep=", ")