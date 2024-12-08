while True:
    num = int(input())

    if num == 0:
        break

    if num % 3 == 0 and num % 7 == 0:
        print("Караул!")
        break
    elif num % 3 == 0:
        print("Несчастливое число")
    elif num % 7 == 0:
        print("Опасное число")
    else:
        print(num)
