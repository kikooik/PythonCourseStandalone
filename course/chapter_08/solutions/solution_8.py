books = []
d = 0
s = 0
while t := input():
    if t == "":
        break
    else:
        p = int(input())
    books.append((t, p))
    
for i in range(len(books)):
    if d > books[i][1]:
        d = d
    elif d < books[i][1]:
        d = books[i][1]
        b = books[i]
print(f"Самая толстая книга: {b}")        

for i in range(len(books)):
    s += books[i][1]
    
print(f"Суммарное число страниц: {s}")