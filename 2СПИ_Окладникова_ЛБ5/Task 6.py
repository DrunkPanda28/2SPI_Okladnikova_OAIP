dict_age = {
    "Archaea": 2800000,
    "Proterozoic": 635000,
    "Paleozoic": 300000,
    "Mesozoic": 145000,
    "Cenozoic": 0
}

text_arr = []

while True:
    text_input = input("Введите возраст: ")
    if text_input == "":
        break
    text_arr.append(int(text_input))

for _t in text_arr:
    if _t >- dict_age["Archaea"]:
        print(_t, ": Archaea")
    elif _t >= dict_age["Proterozoic"]:
        print(_t, ": Proterozoic")
    elif _t >= dict_age["Paleozoic"]:
        print(_t, ": Paleozoic")
    elif _t >= dict_age["Mesozoic"]:
        print(_t, ": Mesozoic")
    elif _t >= dict_age["Cenozoic"]:
        print(_t, ": Cenozoic")
