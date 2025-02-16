import random


class Pet:
    def __init__(self):
        self.name = ''
        self.states = ("несчастным (＃＞＜) ", "уставшим (-_-)", "нормально (＾▽＾)", "довольным (* ^ ω ^)", 'счастливым '
                                                                                                        '＼(￣▽￣)／')
        self.mood = self.states[2]  # Настроение питома
        self.energy = 60  # Сонливость
        self.cleanness = True  # Чистота
        self.contentment = 5  # Довольность
        self.activity = 40  # Хочет играть или нет
        self.run = True  # Запуск программы
        self.order = ""  # взаимодействие с питомцем
        self.hungry = 20  # голод

    # Главный цикл игры
    def run_game(self):
        self.start_game()
        while self.run:
            self.info_pet()
            self.enter_command()
            self.command_processing()
            self.calculation_rezult()
            self.life_pet()

    def enter_command(self):
        self.order = input("Введите одну из команд: покормить, помыть, уложить спать, поиграть, попрощаться: \n")

    # проверяем какое взаимодействие с питомцем проявил пользователь
    def command_processing(self):
        self.contentment = 5
        if self.order.lower() == "покормить":
            self.hungry += 50
            print("Вы покормили своего питомца")
            # рандомное определение на чистоту после приема пищи
            if 1 == random.randint(0, 2):
                self.cleanness = False
                print("Питомец стал грязным")

        elif self.order.lower() == "помыть":
            self.cleanness = True
            print("Вы помыли своего питомца")

        elif self.order.lower() == "уложить спать":
            self.energy = 100
            print("Вы уожили спать своего питомца")

        elif self.order.lower() == "поиграть":
            self.activity += 70
            self.rock_paper_scissors()

        elif self.order.lower() == "попрощаться":
            print("Вы попрощались со своим питомцем")
            self.run = False
        else:
            self.contentment -= 2

    # Добавляет негативные или положительные параметры питомца
    def calculation_rezult(self):
        self.negative_conditions()
        self.positive_conditions()

    # Подсчет негативных параметров
    def negative_conditions(self):
        if not self.cleanness:
            self.contentment -= 1
            print("Питомец грязный")

        if 50 > self.energy > 20:
            self.contentment -= 1
        elif self.energy < 20:
            self.contentment -= 2
            print("Питомец хочет спать")

        if 50 > self.hungry > 20:
            self.contentment -= 1
        elif 20 > self.hungry > 0:
            self.contentment -= 2
            print("Питомец голоден")
        elif self.hungry <= 0:
            self.contentment -= 3
            print("Питомец стал бессмертным и он безумно голоден!!! ((╬◣﹏◢))")

        if 50 > self.activity > 20:
            self.contentment -= 1
        elif self.activity < 20:
            print("Питомец хочет поиграть")

    # Подсчет положительных параметров
    def positive_conditions(self):
        if self.cleanness:
            self.contentment += 1

        if 50 < self.energy < 80:
            self.contentment += 1
        elif self.energy > 80:
            self.contentment += 2

        if 50 < self.hungry < 80:
            self.contentment += 1
        elif self.hungry > 80:
            self.contentment += 2

        if 50 < self.activity < 80:
            self.contentment += 1
        elif self.activity > 80:
            self.contentment += 2

    # Устанавливаем начальные параметры
    def life_pet(self):
        self.energy -= 10
        self.hungry -= 8
        self.activity -= 4
        print()

    def info_pet(self):
        # проверка Довольность питомца
        if self.contentment > 8:
            self.mood = self.states[4]
        elif 7 <= self.contentment <= 8:
            self.mood = self.states[3]
        elif 5 <= self.contentment <= 6:
            self.mood = self.states[2]
        elif 1 <= self.contentment <= 2:
            self.mood = self.states[1]
        else:
            self.mood = self.states[0]
        print(f"{self.name} сейчас чуствует себя {self.mood}")

    def start_game(self):
        self.name = input("Добра пожаловать в игру! \nПридумайте имя своему питомцу: \n")

    def rock_paper_scissors(self):
        print("Питомиц просит поиграть в камень ножницы бумагу.")
        items = ["камень", "бумага", "ножницы"]

        choice = int(input("Введите число: 0 - камень, 1 - бумага, 2 - ножницы.\n"))
        choice_pet = random.randint(0, 2)   # 0 - камень, 1 - бумага, 2 - ножницы

        print(f"Вы выбрали {items[choice]}, а {self.name} показал {items[choice_pet]}")
        if choice == choice_pet:
            print("Ничья (￣︿￣)")
        if choice == 0 and choice_pet == 1:
            print(f"{self.name} победил <(￣︶￣)>")
        if choice == 0 and choice_pet == 2:
            print(f"Вы победили")
        if choice == 1 and choice_pet == 0:
            print(f"Вы победили")
        if choice == 1 and choice_pet == 2:
            print(f"{self.name} победил <(￣︶￣)>")
        if choice == 2 and choice_pet == 0:
            print(f"{self.name} победил <(￣︶￣)>")
        if choice == 2 and choice_pet == 1:
            print(f"Вы победили")
        print("Игра завершина. Вы весело провели время со своим питомцем")


if __name__ == "__main__":
    tamagotchi = Pet()

    tamagotchi.run_game()