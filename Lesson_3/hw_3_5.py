def summa():
    s = 0
    while True:
        a = input("enter: ").split()
        for i in range(len(a)):
            # s = s + a[i]
            try:
                if a[i] == "&&":
                    return s
                else:
                    s = int(a[i]) + s
            except ValueError:
                return s
print(summa())


