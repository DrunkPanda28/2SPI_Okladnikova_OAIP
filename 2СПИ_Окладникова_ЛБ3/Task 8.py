a = input('Введите слово: ')
word = [a]
minimum = [word[0]]
while word[-1] != 'стоп':
    if len(word[-1]) < len(minimum[-1]):
        minimum = [word[-1]]
    word.append(input('Введите слово: '))
print(minimum[0])

