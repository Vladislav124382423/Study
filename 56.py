a = int(input("Enter a:"))
b = int(input("Enter b:"))
c = int(input("Enter c:"))
x = int(input("Enter x:"))
y = int(input("Enter y:"))
if (x >= a) and (y >= b) or (x >= b) and (y >= a):
    print("пройде за ребрами (a & b)")
if (x >= a) and (y >= c) or (x >= c) and (y >= a):
    print("пройде за ребрами (a & c)")
if (x >= b) and (y >= c) or (x >= c) and (y >= b):
    print("пройде за ребрами (a & b)")
