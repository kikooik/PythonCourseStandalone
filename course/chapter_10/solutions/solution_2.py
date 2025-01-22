a = input()
b = input()
l = a.split()
ln = b.split()
u = set(l)
un = set(ln)
el = u & un
l = list(el)
print(*sorted(l))