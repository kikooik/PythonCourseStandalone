s = input()
l = s.split()
l1 = []
for i in l:
    if i.isalpha() == True:
        l1.append(i.capitalize())
    else:
        l1.append(i)
s1 = " ".join(l1)
print(f"Результат: {s1}")