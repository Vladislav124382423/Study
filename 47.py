import  math
x = int(input("enter number"))
y = int(input("enter number"))
z = int(input("enter number"))

if (x < y + z) and (y < x + z):
    print("Трикутник існує")
    math.degrees(x % y % z)


else:
    print("Трикутник не існує")
