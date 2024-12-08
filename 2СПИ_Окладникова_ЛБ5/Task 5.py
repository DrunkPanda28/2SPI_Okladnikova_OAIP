n = int(input("Введите кол-во различных цветов: "))
colors = input("Введите названия цветов (через пробел): ")
m = int(input("Введите кол-во флагов: "))

garland = []
for i in range(m):
    ind = i % n
    garland.append(colors[ind])
print("\n".join(garland))