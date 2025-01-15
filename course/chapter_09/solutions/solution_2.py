l = "аеёиоуэюяАЕОЭЯИЮЁУ"
c = 0
s = input()
for i in s:
    if i in l:
        c += 1
print(f"Количество гласных букв: {c}")