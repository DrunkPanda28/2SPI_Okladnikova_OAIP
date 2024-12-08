x, y, z = map(int, input("Введите ширину длину и высоту большой коробки через пробел: ").split())

total_volume_large_box = x * y * z
total_volume_small_box = 0

while True:
    #Записываем размеры маленькой коробки
    dimensions = list(map(int, input("Введите ширину длину и высоту маленькой коробки (или 0 для завершения):").split()))
    #Если 0 то заканчиваем цикл
    if dimensions[0] == 0:
        break
    #проверяем все ли введены размеры
    if len(dimensions) != 3:
        print("Ошибка введены не все размеры, необходимо ввести все три велечины!!")
        continue

    width, length, height = dimensions
    total_volume_small_box += width * length * height

    #Сравниваем объёмы и выводим результат
    if total_volume_small_box <= total_volume_large_box:
        print('Да')
    else:
        print('нет')