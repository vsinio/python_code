"""
Задание 3.
Реализовать базовый класс Worker (работник),
в котором определить публичные атрибуты name, surname, position (должность),
и защищенный атрибут income (доход). Последний атрибут должен ссылаться
на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать публичные методы
получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
проверить значения атрибутов, вызвать методы экземпляров).
П.С. попытайтесь добить вывода информации о сотруднике также через перегрузку __str__
__str__(self) - вызывается функциями str,print и format. Возвращает строковое представление объекта.

"""
dic_1 = {"wage": 15000, "bonus": 1500}


class Worker:
    """класс содержащий данные работника"""
    name = 'Ivan'
    surname = 'Ivanov'
    position = 'Prod-Tech'
    _income = dic_1


w = Worker()
print(w.__dict__)
print(type(w))


class Position(Worker):
    """дочерний класс воркера с методами"""

    def get_full_name(self):
        """функция отображения name surname"""
        print(f"Bмя сотрудника: {self.name} фамилия: {self.surname}")

    def get_total_income(self):
        """функция отображения зп и премии"""
        print(f"Сотрудник заработал {dic_1['wage']}рублей + премия - {dic_1['bonus']} рублей,"
              f"\nитого: {dic_1['wage'] + dic_1['bonus']}рублей")


w1 = Position()
print(w1.__dict__)
print(type(w1))
print("___________")

ivan = Position()
ivan.get_full_name()
ivan.get_total_income()
