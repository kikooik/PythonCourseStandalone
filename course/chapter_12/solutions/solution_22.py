def check_analysis(**checks):
    max_s = 0
    user = ""
    d = {}
    l = []
    for key, items in checks.items():
        s = sum(items.values())
        if s > max_s:
            max_s = s
            user = key
        for product,i in items.items():
            if product in d:
                d[product] +=1
            else:
                d[product] = 1
                l.append(product)
        max_c = 0
        p = ""
        for product in l:
            c = d[product]
            if c > max_c:
                max_c = c
                p = product
    return (user, p)

