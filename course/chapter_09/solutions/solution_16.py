s = input()
l = s.split()
l1 = []
for i in l:
    l1.append(i[::-1])
print(" ".join(l1))