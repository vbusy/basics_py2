# a[i - 1], a[i] == a[i], a[i - 1]


a = list(input("enter: ").split())
i = 0
while i +1 < len(a):
    if i % 2 ==0:
        elem = a.pop(i+1)
        a.insert(i, elem)
    i = i + 1
print(a)

