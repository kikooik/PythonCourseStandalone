def apply_to_nested_list(nested_list, func):
    l = []
    for i in nested_list:
        if isinstance(i, list):
            l.append(apply_to_nested_list(i, func))
        else:
            l.append(func(i))
    return l