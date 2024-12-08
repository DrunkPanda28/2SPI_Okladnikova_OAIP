import math

n = int(input())
m = int(input())

if m <= 0:
    print("Расстояние за день должно быть положительным.")
else:
    days = math.ceil(n / m)
    print("Спортсмен добежит до финиша на", days, "день.")