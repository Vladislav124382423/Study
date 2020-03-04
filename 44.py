x = int(input("enter number"))
y = int(input("enter number"))
z = int(input("enter number"))
if x and y and z < 1:
    if (x < y) and (y < z):
        x = (y + z)// 2
        print(x)
if (y < x) and (y < z):
    y = (x + z)// 2
    print(y)
else:
    z = (x + y)//2
    print(z)