def count_unique_elements(lst):
    d = {}
    for i in lst:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    return d

