import math
x = int(input("ВВедіть число"))
f = math.modf(x)
print("Ціла частина", f)
r = math.ceil(x)
print("X округлене до найближчого цілого", r)


