def dev(a,b):
    try:
        return (a / b)
    except ZeroDivisionError as err:
        print("Error: ", err)

print(dev(12,6))