def greet_users(*names):
    l = []
    for n in names:
        l.append(f"Привет, {n}!")
    return print(*l, sep="\n")
greet_users("Анна", "Иван", "Мария")