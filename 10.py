import math

print ("Задание 10")

g = 9.81

h = input ("Введите высоту: ")

h = float(h)

t = math.sqrt(2*h/g)

print("Время падения: %.2f" , t)