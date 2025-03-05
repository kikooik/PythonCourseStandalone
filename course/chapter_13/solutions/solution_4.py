def check_all(data, check_func):
    for i in data:
        if check_func(i) == False:
            return False
        else:
            return True