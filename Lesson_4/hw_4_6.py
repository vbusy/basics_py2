from itertools import count
n = int(input("enter: "))
for i in count(n):
    if i > 20:
        break
    print(i)