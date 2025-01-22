s = input()
l = []
for i in s:
    if i != " ":
        l.append(i)
u = set(l)
l = list(u)
print("Уникальные символы:", *sorted(l))