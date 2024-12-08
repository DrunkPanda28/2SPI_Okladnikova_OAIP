number = float(input('Введите число: '))
operation = input('Введите операцию: ')
result = number
while operation != 'стоп':
    number = float(input('Введите число: '))
    if operation == '+':
        result += number
    elif operation == '-':
        result -= number
    elif operation == '*':
        result *= number
    elif operation == '/':
        result /= number
    elif operation == '**':
        result **= number
    print(result)
    operation = input('Введите операцию: ')
