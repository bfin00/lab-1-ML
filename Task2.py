def jacc(a, b):
    u = len(a) + len(b)
    c = 0
    for el in a:
        if el in b:
            c = c + 1
            u = u - 1
    res = c/u
    return res
