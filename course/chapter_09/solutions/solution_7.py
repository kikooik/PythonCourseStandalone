s = input()
letters = 0
numbers = 0
other = 0

for i in s:
    if i.isalpha():
        letters += 1
    elif i.isdigit():
        numbers += 1
    else:
        other += 1
print(f"Количество букв: {letters}")
print(f"Количество цифр: {numbers}")
print(f"Количество других символов: {other}")