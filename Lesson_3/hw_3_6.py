def int_func(a):
    return a.capitalize()

b = input()
print(" ".join(map(int_func, b.split())))