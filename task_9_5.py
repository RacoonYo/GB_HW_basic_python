from PIL import Image
from os import path


class Stationery:
    title = 'Stationery'

    def draw(self):
        return 'Запуск отрисовки'


class Pen(Stationery):
    title = 'Pen'

    def draw(self):
        image = Image.open(path.join('images', 'pen.jpg'))
        image.show()


class Pencil(Stationery):
    title = 'Pencil'

    def draw(self):
        image = Image.open(path.join('images', 'pencil.jpg'))
        image.show()


class Handle(Stationery):
    title = 'Handle'

    def draw(self):
        image = Image.open(path.join('images', 'Handle.jpg'))
        image.show()
