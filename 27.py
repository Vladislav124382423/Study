# Даны действительные положительные числа a, b, с. По трем сторонам с длинами а, Ь, с можно построить треугольник. Найти углы треугольника.
from math import* 

a = float(input('Choose side a: '))

b = float(input('Choose side b: '))

c = float(input('Choose side c: '))


alpha = acos((b**2 + c**2 - a**2) / (2 * b * c))

beta = acos((a**2 + c**2 - b**2) / (2 * b * c))

gamma = acos((b**2 + a**2 - c**2) / (2 * b * c))

a = degrees(alpha)
b = degrees(beta)
c = degrees(gamma)

print (a, b, c)
# cos_a = float( (b**2 + c**2 - a**2) / (2 * b * c) )

# cos_b = float( (a**2 + c**2 - b**2) / (2 * a * c) )

# cos_c = float( (b**2 + a**2 - c**2) / (2 * b * a) )

# alpha = cos(cos_a)
# beta = cos(cos_b)
# gamma = cos(cos_c)

# if (a>0 and b>0 and c>0):
#     print('alpha: ', alpha, '\nbeta:', beta, '\ngamma:', gamma)
# else:
#     print('Your sides is < 0!')
