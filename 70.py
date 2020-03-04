m = int(input("first number:"))
n = int(input("second number:"))
if 0 < m <= 12:
    if 0 <= n < 60:
        res = 60 * (m + 1//(1+(60 * m + 1)//(11 * n + 1))*12)// 11 - n
        print(res)