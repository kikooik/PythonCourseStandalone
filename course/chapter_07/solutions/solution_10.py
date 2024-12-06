toys = []

while n := input():
    if n == "":
        break
    else:
        toys.append(n)
        
while n := input():
    if n == "":
        break
    else:
        toys.append(n)
        
while t := input():
    if t == "":
        break
    elif t not in toys:
        print("такой игрушки нет")
    else:
        toys.remove(t)
        
print(toys)