a = int(input("enter a:"))
b = int(input("enter b:"))
c = int(input("enter c:"))
d = int(input("enter d:"))
e = int(input("enter e:"))
g = int(input("enter g:"))
h = int(input("enter h:"))
x = int()
y = int()
f = int()
f = (x - e) * (h - f) - (y - f) * (g - e)
f_1 = (a - e) * (h - f)- (b - f) * (g - e)
f_2 = (c - e) * (h - f) - (d - f) * (g - e)
if (f_1 > 0) and (f_2 > 0) or (f_1 < 0):
    print('Yes')
else:
    print('No')


