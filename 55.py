a = int(input("Enter a:"))
b= int(input("Enter b:"))
c = int(input("Enter c:"))
d = int(input("Enter d:"))
if (a <= c) and (b <= d) or ( a <= d) and (b <= c):
    print("Прямокутник зі сторонами (a,b) можна помістити всередині прямокутника зі сторонами (c,d)")
else:
    print("Restart")