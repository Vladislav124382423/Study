import math
h = int(input("Enter:"))
a = math.sqrt((math.fabs((math.sin(8 * h)))) + 17)/ (1 - (math.sin(4))* h) * (math.cos(h**2 + 18))**2
b = 1 - math.sqrt(3 / 3 + (math.fabs(math.tan( a * h**2)- math.sin(a * h))))
c = (a * h**2 * math.sin(b * h)) + (b * h**2 * math.cos(a * h))
d = b**2 - 4 * a * c
if d > 0:
    x_1 = (- b + math.sqrt(d)) / 2 * a
    x_2 = (-b - math.sqrt(d)) / 2 * a
    print(x_1, x_2)
else:
    print("Коренів немає")