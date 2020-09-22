arr = ['a', 'b', 'c', 'd' , 'e', 'b']
result = {val: [i for i, val_2 in enumerate(arr) if val_2 == val] for val in arr}
print(result)