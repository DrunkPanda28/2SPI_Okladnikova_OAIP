width = input("Введите трехзначное число: ")

first_digit = int(width[0])
middle_digit = int(width[1])
third_digit = int(width[2])

sum_first_third = first_digit + third_digit

if sum_first_third % 8 != 0 and middle_digit == 3:
    print("Подходит")
else:
    print(sum_first_third, middle_digit)