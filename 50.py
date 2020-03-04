import math
a_1 = int(input("enter number"))
b_1= int(input("enter number"))
c_1 = int(input("enter number"))
a_2 = int(input("enter number"))
b_2= int(input("enter number"))
c_2 = int(input("enter number"))
y = int()
s = math.fabs(a_1 * b_2 - a_2 * b_1)
if s > 0.0001:
    x = a_2 + b_2 * y + c_2
    res = a_1 * x + b_1 + c_1
    print(res)
