def merge_dicts(dict1: dict, dict2: dict):
    d = {}
    for key, values in dict1.items():
        if key in d:
            d[key] = set.union(d[key], values)
        else:
            d[key] = values
    for key, values in dict2.items():
        if key in d:
            d[key] = set.union(d[key], values)
        else:
            d[key] = values
    return d

dict1 = {'a': {1, 2}, 'b': {3, 4}}
dict2 = {'b': {5}, 'c': {6, 7}}
print(merge_dicts(dict1, dict2))