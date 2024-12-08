word = input("Введите слово: ")
n = int(input("Введите натуральное число: "))

if n > 0:
    for i in range(1, n + 1):
        print(word)
else:
    print("Пожалуйста, введите натуральное число.")