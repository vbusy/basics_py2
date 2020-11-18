def salary(time, rate, prize):
    sal = time * rate + prize
    return sal

from sys import argv
script_name, x, y, z = argv

d = salary(int(x, y, z))
print("Salary employees: ", d)