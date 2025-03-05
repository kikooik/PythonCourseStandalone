def apply_functions_sequence(data, func_list):
    l = []
    for i in data:
        for f in func_list:
            i = f(i)
        l.append(i)
    return l