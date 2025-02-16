class Buttom:
    def __init__(self, text, activne=False, color="blue", size="medium"):
        self.text = text
        self.acrivne = activne
        self.color = color
        self.size = size

    # Проверка активации кнопки
    def pressed(self):
        if self.acrivne:
            print("Кнопка активирована!")
        else:
            print("Кнопка не была активирована!")

    def color_changed(self, new_color):
        if self.acrivne:
            self.color = new_color
            print(f"После активации кнопки, цвет был изменён на {new_color}!")

    def __str__(self):
        print(f"Buttom: \n text: {self.text} \n color: {self.color}\n size: {self.size}")


if __name__ == "__main__":
    buttom = Buttom("Записаться", activne=True)

    buttom.pressed()
    buttom.color_changed("pink")
    buttom.__str__()
