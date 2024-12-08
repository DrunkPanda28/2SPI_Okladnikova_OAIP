a = int(input("Введите кол-во номеров: "))
digits = set()
for i in range(a):
    digits |= set(input("Введите номер: "))
print(len(digits))