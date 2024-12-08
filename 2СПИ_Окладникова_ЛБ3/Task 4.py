
user_input = input("Введите числа через пробел: ")
numbers = list(map(float, user_input.split()))

smallest = numbers[0]

for num in numbers:
    if num < smallest:
        smallest = num

print("Наименьшее число:", smallest)
