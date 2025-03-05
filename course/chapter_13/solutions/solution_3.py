def apply_multiple(data, func1, func2):
    l = []
    for i in data:
        i1 = func1(i)
        l.append(func2(i1))
    return l