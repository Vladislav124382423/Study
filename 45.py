import  math
a = int(input("enter number"))
b = int(input("enter number"))
c = int(input("enter number"))
d = int(input("enter number"))
max(a, b, c, d)
if (a <= b) and (b <= c) and (c <= d):
    max = a
    if (b > max):
        max = b
        if(c > max):
            max = c
        if(d > max):
            max = d
            print(max)
if (a > b) and (b > c) and (c > d):
    a = math.sqrt(a)
    b = math.sqrt(b)
    c = math.sqrt(c)
    d = math.sqrt(d)
    print(a,b,c,d)
else:
    print("error")