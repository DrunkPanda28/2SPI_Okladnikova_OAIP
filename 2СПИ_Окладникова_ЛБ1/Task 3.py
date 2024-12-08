a = int(input())
digits_of_number = []

for i in range(3):
    b = a % 10
    a = a // 10
    digits_of_number.append(b)

digits_of_number.append(a)

print(str(digits_of_number[0]), " - 1p")
print(str(digits_of_number[1]), " - 10p")
print(str(digits_of_number[2]), " - 100p")
print(str(digits_of_number[3]), " - 1000p")