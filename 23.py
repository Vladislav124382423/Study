import math
print("Введите a:")
a = float(input())
print("Введите b:")
b = float(input())
print("Введите c:")
c = float(input())
lh = math.sqrt(a + b + c)
m = math.sqrt(2 * a**2 + 2 * b**2 - c**2)/2

print("Result:", lh)
print("Result:", m)

