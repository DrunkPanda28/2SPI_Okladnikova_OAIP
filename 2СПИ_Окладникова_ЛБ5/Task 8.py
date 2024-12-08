decimal_number = input("Введите десятичное число: ")
all_list_numbers = []
list_numbers = []
_list_numbers = decimal_number.split()

for _l in _list_numbers:
    list_numbers.append(int(_l))

for _number in list_numbers:
    dict_data = {}
    binary_number = ''
    digits = 0
    units = 0
    zeros = 0

    if _number == 0:
        binary_number = '0'
    else:
        while _number > 0:
            digits += 1
            remainder = _number % 2
            if _number % 2 == 0:
                zeros += 1
            elif _number % 2 != 0:
                units += 1
            binary_number = str(remainder) + binary_number
            _number = _number // 2

    dict_data["digits"] = digits
    dict_data["units"] = units
    dict_data['zeros'] = zeros
    all_list_numbers.append(dict_data)

print(all_list_numbers)