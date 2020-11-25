from functools import reduce

def list_mult():
    list_2 = [i for i in range(100, 1001) if i % 2 == 0]
    return list_2

# print(list_mult())
print(reduce(lambda a,b: a * b, list_mult()))