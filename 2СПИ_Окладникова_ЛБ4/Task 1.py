a = []
for i in range(1, 9):
    a.append((input("Введите " + str(i) + " разряд: ")))
print(''.join(map(str, a)))