def apply_to_all(data, func):
    l = []
    for i in data:
        l.append(func(i))
    return l