print ("Задание 7")

v1 = input("Введите объем первой жидкости: ")
t1 = input("Введите температуру первой жидкости: ")

v1 = float(v1)
t1 = float(t1)

v2 = input("Введите объем второй жидкости: ")
t2 = input("Введите температуру второй жидкости: ")

v2 = float(v2)
t2 = float(t2)

tc = (v1 * t1 + v2 * t2) / (v1 + v2)
vc = v1 + v2

print("Итоговый объем: %.2f" % vc)
print("Итоговая теспература: %.2f" , tc)