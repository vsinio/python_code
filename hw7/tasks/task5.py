"""
Задание 5.
Реализовать класс Stationery (канцелярская принадлежность).
Определить в нем публичный атрибут title (название) и публичный метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.”
Создать три дочерних класса: Pen (ручка), Pencil (карандаш), Handle (маркер).
В каждом из классов реализовать переопределение метода draw.
Для каждого из классов метод должен выводить уникальное сообщение.
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""
class Stationery:
    """main class for others children"""
    def __init__(self,title="Канцелярская принадлежность =)"):
        self.title=title
    def draw(self):
        """func print string"""
        print("Запуск отрисовки.")

class Pen(Stationery):
    """child class from Stationery"""
    def draw(self):
        """new func for new class"""
        print("Запуск отрисовки ручки? \nДа!")
class Pencil(Stationery):
    """child class from Stationery"""
    def draw(self):
        """new func for new class"""
        print("Запуск отрисовки карандаша? \nДа!")
class Handle(Stationery):
    """child class from Stationery"""
    def draw(self):
        """new func for new class"""
        print("Запуск отрисовки маркера? \nДа!")

s = Stationery()
pen = Pen("ручка")
pencil = Pencil("карандаш")
handle = Handle("маркер")

print(type(pen))
print(type(pencil))
print(type(handle))
print()
s.draw()
pen.draw()
pencil.draw()
handle.draw()
