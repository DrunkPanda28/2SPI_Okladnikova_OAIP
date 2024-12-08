empty_dict = {}
print(empty_dict)

my_dict = {'имя': "Иван",
           "фамилия": "Павлов",
           "возраст": 21}

print(my_dict)

my_dict["профессия"] = "инженер"

print(my_dict)

del my_dict["возраст"]
print(my_dict)

my_dict["фамилия"] = "Иванов"
print(my_dict)