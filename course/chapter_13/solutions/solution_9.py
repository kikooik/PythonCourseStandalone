def transform_list(data, transform_func, condition_func):
    l = []
    for i in data:
        if condition_func(i):
            l.append(transform_func(i))
        else:
            l.append(i)
    return l