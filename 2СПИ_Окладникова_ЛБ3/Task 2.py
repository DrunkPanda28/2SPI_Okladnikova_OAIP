count = 0

while True:
    num = float(input())
    if num > 36.6:
        break
    if num < 0:
        count += 1

print(count)
