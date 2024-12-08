buyers_day_before_yesterday = int(input("Введите число покупателей позавчера: "))
buyers_yesterday = int(input("Введите число покупателей вчера: "))

defference = buyers_yesterday - buyers_day_before_yesterday

if defference > 0:
    buyers_today = buyers_yesterday + defference
else:
    buyers_today = buyers_yesterday - abs(defference)

print("Сегодня магазин посетит:", buyers_today)