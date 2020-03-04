import  math
a1 = int(input("enter number"))
b1 = int(input("enter number"))
c1 = int(input("enter number"))
y = int()
x = y**2

r = a1 * (x**4) + b1 * (x**2) + c1
d = (b1) **2 - 4 * a1 * c1
y1 = (- b1) + math.sqrt(d) / 2 * 16
y2 = (- b1) - math.sqrt(d) / 2 * 16
if d > 0:

    print(d)
if d < 0:
    print("Result is null")
