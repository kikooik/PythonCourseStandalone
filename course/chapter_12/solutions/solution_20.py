def find_max(a, b, *args):
    l = [a, b]
    for n in args:
        l.append(n)
    return max(l)