s = int(input("Phi:"))
hours, minutes = divmod(s, 30)
minutes *= 12
print(f"{hours} годин {minutes} хвилин")