s = input()
l = s.split()
ln = []
for i in l:
    if len(i) == 1:
        ln.append(i)
    else:
        a = i[0] + i[-1]
        ln.append(a)
f = " ".join(ln)
print(f"Результат: {f}")        