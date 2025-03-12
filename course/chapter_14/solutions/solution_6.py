def multiples_of_3_and_5(n):
    l = [x for x in range(n) if x % 3 == 0 and x % 5 == 0]
    return l