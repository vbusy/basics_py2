a = [9, 8, 6, 6, 5, 5, 4, 4]
n = int(input("new: "))
i = 0
for s in a:
    if n <= s:
        i = i + 1
a.insert(i, n)
print(a)


