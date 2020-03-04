from random import randint
n = int(input("n = "))



def create_list(row):
    a = []
    for i in range(row):
        a.append(randint(a[1], a[n]))
        return a
    res = (a[1] + a[n])
    print (res)
