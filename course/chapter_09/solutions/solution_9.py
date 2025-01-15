s = input()
s1 = ""

for i in s:
    if i.isdigit() == False:
        s1 += i
print(s1)