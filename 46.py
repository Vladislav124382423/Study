import  math
x = int(input("enter number"))
y = int(input("enter number"))
if x and y < 0:
    x = abs(x)
    y = abs(y)
    print(x, y)
if x  and y < 0:
    print(math.fabs(x % y))
    if (x > 0) and (y < 0):
        s = (x, y) + 0.5
        print(s)


