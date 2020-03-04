import math
x_1 = int(input("enter x1:"))
x_2 =int(input("enter x2:"))
x_3 =int(input("enter x3:"))
y_1=int(input("enter y1:"))
y_2 =int(input("enter y2:"))
y_3 =int(input("enter y3:"))
def S(x_1, x_2, x_3, y_1, y_2, y_3):
    a = math.sqrt(((x_1 + x_2)**2) +((y_1 - y_2)**2))
    b = math.sqrt(((x_2 - x_3)**2) + ((y_1 - y_3)**2))
    c = math.sqrt(((x_1 - x_3)**2) + ((y_1 - y_3)**2))
    p = (a + b + c)/2
    S = math.sqrt(p * (p - a) * (p - b) * (p - c))

if (S(x_1, x_3, 0, y_1, y_3, 0)) + (S(x_2, x_3, 0, y_2, y_3, 0)) +(S(x_1, x_2, 0, y_1, y_2, 0)) > (S(x_1, x_2, x_3, y_1, y_2, y_3)):
    print("Y")
else:
    print("N")

