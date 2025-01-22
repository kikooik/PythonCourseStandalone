a = input()
b = input()
l = a.split()
ln = b.split()
u = set(l)
un = set(ln)
dif = u ^ un
l = list(dif)
print(*sorted(l))