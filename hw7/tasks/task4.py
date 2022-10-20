
"""
Задание 4.
Реализуйте базовый класс Car. У данного класса должны быть следующие публичные атрибуты:
speed, color, name, is_police (булево).
А также публичные методы: go, stop, turn(direction),
которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс публичный метод show_speed,
который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar)
и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""
from random import randint


class Car:
    """класс содержащий данные об авто"""
    speed = randint(1, 100)

    def __init__(self, speed, color="red", name="BMW", is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        """функция - машина поехала + ранд скорость из инита"""
        print(f"Машина поехала вперед со скоростью {self.speed}")

    def stop(self):
        """функция выводящая остановку"""
        print("Машина остановилась.")

    def turn(self):
        """поворот авто на рандом"""
        direction = randint(1, 2)
        print("Машина повернула налево") if direction == 1 else print("Машина повернула направо")

    def show_speed(self):
        """оказывает скорость авто"""
        print(f"В данный момент машина движется со скоростью {self.speed}")


class TownCar(Car):
    def show_speed(self):
        """показ предупреждения авто"""
        if self.speed > 60:
            print("WARNING!!! Сбросьте скорость")
            print(f"В данный момент машина движется со скоростью {self.speed}")

class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        """показ предупреждения авто"""
        print(f"В данный момент машина движется со скоростью {self.speed}")
        if self.speed > 40:
            print("WARNING!!! Сбросьте скорость")
        else:
            pass


class PoliceCar(Car):
    pass


town = TownCar(randint(1, 100), "Blue", "Mercedes")
sport = SportCar(randint(1, 100), "Green", "Lada")
work = WorkCar(randint(1, 100), "Black", "Audi")
pol = PoliceCar(randint(1, 100), "Yellow", "Bugatti", True)

print(f'TownCar = {town.__dict__}')
town.show_speed()
print(f'SportCar = {sport.__dict__}')
print(f'WorkCar = {work.__dict__}')
work.show_speed()
print(f'PoliceCar = {pol.__dict__}')
