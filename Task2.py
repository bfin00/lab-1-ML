m = [4, 5]
n = [1, 4, 6, 5]
def jaccard(a, b):
    q1 = 0
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] == b[j]:
                q1 = q1 + 1
                break
    d = dict()
    for i in range(len(a)):
        d[a[i]] = i
    for i in range(len(b)):
        d[b[i]] = i
    q2 = len(d)
    return q1/q2
            
print(jaccard(m, n))