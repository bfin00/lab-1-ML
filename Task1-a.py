arr = ['a', 'b', 'c', 'd' , 'e', 'a', 'd']
a = 0
d = dict()
for i in range(len(arr)):
    tar = arr[i]
    t = []
    arr_t = arr
    try:
        while(len(arr_t) > 0):
            x = arr_t.index(tar)
            t.append(x)
            arr_t = arr_t[(x+1):]
    except ValueError:
        arr_t.clear()
    d[arr[i]] = t
print(d)   
