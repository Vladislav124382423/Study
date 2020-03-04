print ("Задание 6")

import math

AB = input("Введите длину первого катета: ")
AC = input("Введите длину второго катета: ")

AB = float(AB)
AC = float(AC)

BC = math.sqrt(AB**2 + AC**2)

S = (AB * AC) / 2

print("Площадь треугольника: %.2f" , S)
print("Гипотенуза треугольника: %.2f" , BC)