result = ''
while True:
    words = input('Введите слово или "!": ')
    if words == 'стоп':
        break

    result += words + ' '

    if words == '!':
        result = result[:-3] + '!'
        result += '\n'

print(result)
