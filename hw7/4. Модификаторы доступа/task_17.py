# класс Transport
class Transport:
    def show_info(self):
        print("Родительский метод класса Transport")


# класс Auto, наследующий Transport
class Auto(Transport):
    def show_info(self):
        print("Родительский метод класса Auto")


# класс Bus, наследующий Transport
class Bus(Transport):
    def show_info(self):
        print("Родительский метод класса Bus")


t = Transport()
t.show_info()

a = Auto()
a.show_info()

b = Bus()
b.show_info()

"""
Родительский метод класса Transport
Родительский метод класса Auto
Родительский метод класса Bus
"""
