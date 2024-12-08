dict_birds = {
    "Swallow": 0,
    "Goldfinch": 0,
    "Heron": 0,
}

while True:
    dict_input = input()
    if dict_input == "":
        break

    bird = dict_input.split(': ')[0]
    count = int(dict_input.split(": ")[1])

    dict_birds[bird] += count

print(dict_birds)