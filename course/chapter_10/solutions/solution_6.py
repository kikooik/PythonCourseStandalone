a = input()
b = input()
l = []
ln = []
for i in a:
    l.append(i)
for i in b:
    ln.append(i)
u = set(l)
un = set(ln)
w = u & un
l = list(w)
p = sorted(l)
print(*p)