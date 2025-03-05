def multi_criteria_sort(data, func1, func2):
    return sorted(data, key=lambda x: (func1(x), func2(x)))
    