def find_anagrams(word_list):
    d = {}
    for i in word_list:
        if i in d.keys():
            break
        else:
            d[i] = []
            for n in word_list:
                if n != i and n not in d[i]:
                    n1 = sorted(n)
                    if n1 == sorted(i):
                        d[i].append(n)
    return d
word_list = ["listen", "silent", "enlist", "hello", "loleh"]
print(find_anagrams(word_list))