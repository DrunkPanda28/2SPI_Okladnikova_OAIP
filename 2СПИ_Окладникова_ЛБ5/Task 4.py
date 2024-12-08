numbers_input = []
numbers_output = []

while True:
    text_input = input('')
    if text_input == "":
        break
    numbers_input.append(int(text_input))

for _n in numbers_input:
    if _n % 2 == 0:
        numbers_output.append(_n)
print(numbers_output)