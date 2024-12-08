text = input("Оцените развлекательный комплекс; ")

words = ["весело", "увлекательно", "развлечения"]

print("Результат анализа; ", end='')
for word in words:
    index = text.find(word)
    print(index, end=' ')