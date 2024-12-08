year = int(input("Введите год: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "является високосным годом.")
else:
    print(year, "не является високосным годом.")
