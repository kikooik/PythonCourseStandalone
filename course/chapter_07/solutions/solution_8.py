guests = []

while n := input():
    if n == "":
        break
    else:
        guests.append(n)
        
while n := input():
    if n == "":
        break
    else:
        guests.append(n)
        
d = input()
guests.remove(d)

print(guests)