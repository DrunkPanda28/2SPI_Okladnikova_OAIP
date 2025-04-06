#  Родительский класс
class Сoldsteel:
    pass


#   Клинковое
class Bladed(Сoldsteel):
    pass


# Колющее
class Stabbing(Bladed):
    pass


class Tridents(Stabbing):
    pass


class Swords(Stabbing):
    pass


class Cutlasses(Stabbing):
    pass


class Spear(Stabbing):
    pass


# Не клинковое
class Notbladed(Сoldsteel):
    pass


# Ударно-Раздробляющее
class Shockcrushing(Notbladed):
    pass


class Brassknuckles(Shockcrushing):
    pass


class Palmpads(Shockcrushing):
    pass


class Combatgloves(Shockcrushing):
    pass


class Maces(Shockcrushing):
    pass


class Flippers(Shockcrushing):
    pass


class Extinguishers(Shockcrushing):
    pass


class TheMace(Shockcrushing):
    pass


class Batons(Shockcrushing):
    pass

