class Character:
    def __init__(self, name, hp, attack_power):
        self.name = name
        self.hp = hp
        self.attack_power = attack_power

    def attack(self):
        return f"{self.name} наносит {self.attack_power} урона!"

    def info(self):
        return f"Персонаж: {self.name}, Здоровье: {self.hp}, Сила атаки: {self.attack_power}"


class Warrior(Character):
    def __init__(self, name, hp, attack_power, armor):
        super().__init__(name, hp, attack_power)
        self.armor = armor

    def attack(self):
        return f"{self.name} атакует ближним боем и наносит {self.attack_power} урона!"

    def defend(self):
        return f"{self.name} использует броню для защиты, снижение урона на {self.armor}."


class Mage(Character):
    def __init__(self, name, hp, attack_power, mana):
        super().__init__(name, hp, attack_power)
        self.mana = mana

    def attack(self):
        return f"{self.name} использует магию и наносит {self.attack_power} урона!"

    def cast_spell(self, spell_cost):
        if self.mana >= spell_cost:
            self.mana -= spell_cost
            return f"{self.name} использует заклинание и тратит {spell_cost} маны!"
        else:
            return f"{self.name} недостаточно маны для заклинания."


class Archer(Character):
    def __init__(self, name, hp, attack_power, arrows):
        super().__init__(name, hp, attack_power)
        self.arrows = arrows

    def attack(self):
        return f"{self.name} стреляет из лука и наносит {self.attack_power} урона!"

    def shoot_arrow(self):
        if self.arrows > 0:
            self.arrows -= 1
            return f"{self.name} выпускает стрелу, осталось стрел: {self.arrows}."
        else:
            return f"{self.name} нет стрел для стрельбы!"


# Пример использования
warrior = Warrior(name="Варвар", hp=100, attack_power=15, armor=5)
mage = Mage(name="Маг", hp=80, attack_power=12, mana=30)
archer = Archer(name="Лучник", hp=90, attack_power=10, arrows=20)

print(warrior.info())
print(warrior.attack())
print(warrior.defend())
print()

print(mage.info())
print(mage.attack())
print(mage.cast_spell(10))
print(mage.cast_spell(25))
print()

print(archer.info())
print(archer.attack())
print(archer.shoot_arrow())
print(archer.shoot_arrow())