import math

print ("Задание 8")

r = input ("Введите радиус окружности: ")
n = input ("Введите количество стоврон: ")

r = float(r)
n = int(n)

pi = 3.14

a = (2 * r * math.tan(pi/n))

per = a * n

print("Периметр: %.2f" , per)