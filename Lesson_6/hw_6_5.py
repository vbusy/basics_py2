class Stationery:
    title = "Stationary"

    def draw(self):
        print("Запуск отрисовки")

class Pen(Stationery):
    title = "Pen"

    def draw(self):
        super().draw()
        print("Рисуем ручкой")


class Pensil(Stationery):
    title = "Карандаш"

    def draw(self):
        super().draw()
        print("Рисуем карандашом")


class Handle(Stationery):
    title = "Ручка2"

    def draw(self):
        super().draw()
        print("Рисуем еще ручкой")


s = Stationery()

p = Pen()
p.draw()

pens = Pensil()
pens.draw()

h = Handle()
h.draw()