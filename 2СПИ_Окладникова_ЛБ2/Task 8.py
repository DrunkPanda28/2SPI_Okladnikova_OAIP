prices = []
for i in range(3):
    price = float(input(f'Введите цену товара {i + 1}: '))
    prices.append(price)

total = sum(prices)
if prices == sorted(prices):
    print("Акция! Общая сумма:", total / 2)
elif prices == sorted(prices, reverse=True):
    print("Акция! Общая сумма:", total / 3)
else:
    print("К оплате:", total)