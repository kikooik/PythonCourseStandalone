db = (
         ("Дмитрий", [4, 3, 5, 4]),
         ("Ольга", [3, 2, 3]),
         ("Михаил", [5, 4, 4, 5]),
         ("Арсений", [5, 2, 4, 2]),
         ("Ксения", [5, 5, 5]),
         ("Марк", [5, 5, 5])
        )

for i in range(len(db)):
    print(db[i][0], *db[i][1])