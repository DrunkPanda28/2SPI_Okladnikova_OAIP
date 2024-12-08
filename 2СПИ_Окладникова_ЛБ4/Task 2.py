n = int(input("Количество имён: "))
names = []

for i in range(n):
    name = input("Введите имя: ")
    names.append(name)

for i in range(n):
    print(i + 1, '-', names[i])