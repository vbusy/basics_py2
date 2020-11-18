from itertools import cycle

x = 0
n = input("enter: ")
for i in cycle(n):
    if x > 15:
        break
    print(i)
    x += 1