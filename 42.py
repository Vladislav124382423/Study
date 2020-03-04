x = int ( input ("enter first number:"))
y = int ( input ("enter first number:"))
s = (x + y) / 2
p = 2 * x * y
if x > 0:
    x = s
    y = p
    print(x, y)
else:
    x = p
    y = s
    print(x,y)
