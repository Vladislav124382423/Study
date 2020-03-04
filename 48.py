import  math
a = int(input("enter number"))
b = int(input("enter number"))
c = int(input("enter number"))
d = b**2 - (4 * a) * c
if d > 0:
    x_1 = (- b + math.sqrt(d))/2 * a
    x_2 = (-b - math.sqrt(d))/2 * a
    print("Result", x_1 , x_2)
else:
    print("Коренів немає")
