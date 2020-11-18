def get_res(list_1):
    list_2 = []
    for  i in range(1, len(list_1)):
        if list_1[i] > list_1[i - 1]:
            list_2.append(list_1[i])
    return list_2

list_1 = [int(i) for i in input().split()]
c = get_res(list_1)
print(c)