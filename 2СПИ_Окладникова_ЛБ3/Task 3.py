numbers = []

while True:
    num = float(input())
    if abs(num) >= 1000:
        break
    numbers.append(num)

max1 = max(numbers)
numbers.remove(max1)
max2 = max(numbers)
print(max2)
