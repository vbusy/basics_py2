# первое решение
# def my_func(x, y):
#     return 1 / (x**y)
# print(my_func(4,-2))

# второй вариант
def my_func(x, y):
    mul = 1
    for i in range(y):
        mul = mul * x
    return 1 / mul
print(my_func(5,2))
