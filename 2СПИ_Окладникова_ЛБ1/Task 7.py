number = int(input("Введите номер буквы (от 1 до 26): ")) - 1

alphabet = "ABCDFGHIJKLMNOPQRSTUVWXYZ"

result = []
for i in range(4):
    result.append(alphabet[(number + i) % 26])
print("".join(result))