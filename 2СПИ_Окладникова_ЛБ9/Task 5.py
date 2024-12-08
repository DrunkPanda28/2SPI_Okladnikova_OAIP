while True:
    try:
        num1 = int(input("Введите первое целое число: "))
        num2 = int(input("Введите второе целое число: "))

        # Попытка деления
        result = num1 / num2  # Замените на int_num1 // int_num2, если нужно целочисленное деление
        print(f"Результат деления: {result}")
        break  # Выход из цикла, если ввод корректен

    except ValueError:
        # Обработка исключения, если ввод не является целым числом
        print("Ошибка: одно из введенных значений не является целым числом. Пожалуйста, введите числа заново.")
    except ZeroDivisionError:
        # Обработка исключения деления на 0
        print("Ошибка: деление на 0 невозможно. Пожалуйста, введите другое второе число.")

print("Выход из программы.")
