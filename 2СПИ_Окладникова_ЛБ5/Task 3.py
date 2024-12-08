digits = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
num = input("Введите число: ")
num_set = set()

for i in num:
    num_set.add(i)
print(' '.join(digits - num_set))