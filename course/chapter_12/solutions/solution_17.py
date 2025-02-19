def count(s):
    s1 = "аоэыуеяиюё"
    c = 0
    for i in s:
        if i in s1:
            c += 1
    return c

def join_strings(*strings): 
    l = []
    l1 = []
    for s in strings:
        l.append(count(s))
    m = max(l)
    for s in strings:
        if count(s) == m:
            l1.append(s)
    if len(l1) > 1:
        return sorted(l1)
    else:
        return l1[0]

