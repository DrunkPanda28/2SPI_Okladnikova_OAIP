class Chest:
    def __init__(self, name, is_locked):
        self.name = name
        self.is_locked = is_locked
        self.container = {}  # Содержимое сундука

    def unlock(self):
        # Открытый сундук
        if self.is_locked:
            print(f"Сундук открыт. Доступных мест: {150 - sum(self.container.values())} из 150")
            self.is_locked = True
        else:
            print("Сундук закрыт")
        return self.container

    def add_item(self, item, count=1):
        # Добавление предмета в сундук
        if self.is_locked and sum(self.container.values()) < 150:
            # self.container.get(item)
            # проверяем наличие предмета в сундуке, если он имеется увеличиваем его значение
            self.container[item] = self.container.get(item, 0) + count
            print(f"{item} добавлен в сундук.")

        elif sum(self.container.values()) > 150:
            print("Сундук переполнен")
        else:
            print("Сундук закрыт, для добавления предмета, нужно открыть сундук")
        return f"Содержимое сундука: {' '.join(self.container)}"

    def remove_item(self, item, count=1):
        # удаляем предмет из сундука
        if self.is_locked:
            # Если такой предмет имеется в сундуке и указанное значение совпадает со значением в сундуке,
            # удаляем предмет полностью
            if item in self.container:
                if count == self.container[item].values():
                    del self.container[item]
                # если указанное кол-во меньше, то просто вычитаем
                else:
                    self.container[item] = self.container.get(item, 0) - count
            else:
                print(f"{item} не найден в сундуке")
        else:
            print("Сундук закрыт! Для удаления предмета, откройте сундук")

    def check_container(self):
        # Проверка содержимого сундука
        if self.is_locked:
            if self.container:
                print(f"Содержимое сундука: ")
                for key, value in self.container.items():
                    print(key, ':', value)
            else:
                print("Судук пустой.")
        else:
            print("Сундук закрыт! Откройте чтобы посмотреть содержимое.")

    def block(self):
        # Открытый сундук
        if not self.is_locked:
            print("Сундук закрыт")
            self.is_locked = True


if __name__ == "__main__":
    treasure_chest = Chest("Сундук сокровищ", True)

    treasure_chest.unlock()
    treasure_chest.check_container()

    treasure_chest.add_item("яблоко", 4)
    treasure_chest.add_item("меч", 2)
    treasure_chest.add_item("яблоко", 2)
    treasure_chest.check_container()
