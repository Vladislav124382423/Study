import  math
r = int(input())
m = int(input())
x = int(input())
y = int(input())
z = int(input())
if r < m:
    r = m**2
    print("res:", r)
    if r > m**2:
        math.fabs(x % y % z)
        print("res:", x % y % z)

