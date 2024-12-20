books = []
d = 0
s = 0
while t := input():
    if t == "":
        break
    else:
        p = int(input())
    books.append((t, p))
    
(print(books))
for i in range(len(books)):
    if d > books[i][1]:
        d = d
    elif d < books[i][1]:
        d = books[i][1]
        

for i in range(len(books)):
    s += books[i][1]
    
print(f"Суммарное число страниц: {s}")