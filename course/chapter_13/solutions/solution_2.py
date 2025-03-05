def filter_data(data, filter_func):
    l = []
    for i in data:
        if filter_func(i):
            l.append(i)
    return l