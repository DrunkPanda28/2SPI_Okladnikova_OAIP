word1 = set(input("Введите 1 слово: "))
word2 = set(input("Введите 2 слово: "))
word3 = set(input("Введите 3 слово: "))
print(''.join(word1 & word2 | word1 & word3 | word2 & word3))