def uniqueness(set_list):
    s = set_list[0]
    s1 = set_list[1]
    s2 = set_list[2]
    u = set.difference(s, s1, s2)
    u1 = set.difference(s1, s, s2)
    u2 = set.difference(s2, s1, s)
    w = set.union(u, u1, u2)
    return w