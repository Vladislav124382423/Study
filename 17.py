print ("Задание 17")

import math

R2 = 20
pi = 3.14

R1 = input ("Введите внешний радиус кольца (>20)")

R1 = int(R1)

S = (pi*abs(R1*R1+R2*R2))
print ("Площадь кольца: %.2f" % S)
input ("Нажмите ENTER для выхода")
