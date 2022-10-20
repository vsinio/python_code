"""
Задание 1.
Создать класс TrafficLight (светофор)
и определить у него один приватный атрибут color (цвет) и публичный метод running (запуск).
В рамках метода running реализовать переключение светофора в режимы:
красный, желтый, зеленый. Продолжительность первого состояния (красный)
составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) —
на ваше усмотрение.
Для имитации "горения" каждого цвета испольщуйте ф-цию sleep модуля time
Переключение между режимами должно осуществляться только
в указанном порядке (красный, желтый, зеленый).
Проверить работу примера, создав экземпляр и вызвав описанный метод.
"""
from time import sleep


class TrafficLight:
    """Это класс содержащий в себе аргументы цветов светофора и функцию вызова его работы"""
    color = ['Красный', 'Желтый', 'Зеленый']

    def running(self):
        """запускает светофор, lst - промежутки delay"""
        lst = [7, 2, 5]

        for sec in range(3):
            print(self.color[sec])
            sleep(lst[sec])


t = TrafficLight()
t.running()

# 2 var
# class TrafficLight_1:
#     color = 'red'
#
#     def running(self):
#         print(self.color)
#         sleep(7)
#         self.color = 'yellow'
#         print(self.color)
#         sleep(2)
#         self.color = 'green'
#         sleep(5)
#         print(self.color)
#
#
# print(TrafficLight_1.__dict__)
# t = TrafficLight_1()
# t.running()
