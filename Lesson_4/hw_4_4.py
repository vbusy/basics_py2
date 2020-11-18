def max_elem(list_12):
    list_2 = [i for i in list_12 if list_12.count(i) == 1]
    return list_2

# list_1 = [int(i) for i in input().split()]
list_12 = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
c = max_elem(list_12)
print(c)