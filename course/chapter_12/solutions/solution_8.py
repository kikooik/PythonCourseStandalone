def swap_keys_values(d):
    new_d = {}
    for key, value in d.items():
        new_d[value] = key
    return new_d