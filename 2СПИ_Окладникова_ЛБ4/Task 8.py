phone_number = input("Введите номер телефона: ")

if not all(char.isdigit() or char == "+" for char in phone_number):
    print("Неправильное номер телефона!")
else:
    print("Номер телефона принят.")