word = input("Введите слово: ")

length = len(word)
if length % 2 == 1:
    middle_index = length // 2
    result = word[middle_index]
else:
    result = word[length // 2 - 1]
print("Результат:", result)