# Базовый класс
class Gravitydefied:
    def __init__(self, position, velocity):
        self.position = position
        self.velocity = velocity

    # Состояние обйекта
    def update(self):
        pass

    # Отображение героя
    def draw(self):
        pass


# Самокат
class Vehicle(Gravitydefied):
    def __init__(self, position, velocity, fuel):
        super.__init__(position, velocity)
        self.fuel = fuel

    # Ускорение
    def accelerate(self, amount):
        pass

    # Торможение
    def brake(self):
        pass

    #Заправка топливо
    def refuel(self, amount):
        pass

# Препятствие
class Obstacle(Gravitydefied):
    def __init__(self, obstacles):
        self.obstacles = obstacles

    # Нахождение Столкновения
    def load(self):
        pass

    # Перезагрузка
    def reset(self):
        pass

# Управление процессом игры
class Game:
    def __init__(self, level):
        self.level = level
        self.vehicle = None

    #Старт игры
    def start(self):
        pass

    # Обновление игры
    def update(self):
        pass

    # Завершение
    def render(self):
        pass

    def end(self):
        pass

