def intersect_lists(lst1, lst2):
    l = list()
    s1 = set(lst1)
    s2 = set(lst2)
    u = set.intersection(s1, s2)
    return list(u)