def fact(a):
    k = 1
    for i in range(1, a + 1):
        k = k * i
        yield k

n = int(input("enter: "))

for el in fact(n):
    print(el, end='\n')
