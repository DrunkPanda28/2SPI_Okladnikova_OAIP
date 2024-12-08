number = int(input("Введите число: "))
sum = 0
for i in range(1, number):
    if number % i == 0:
        sum += 1
print(number + sum)