class Auto:
    # атрибуты класса
    auto_count = 0

    # методы класса
    def on_auto_start(self, auto_name, auto_model, auto_year):
        print("Автомобиль заведен")
        self.auto_name = auto_name
        self.auto_model = auto_model
        self.auto_year = auto_year
        Auto.auto_count += 1


a = Auto()
a.on_auto_start("Lexus", "RX 350L", 2019)
print(a.auto_name)
print(a.auto_count)

"""
Автомобиль заведен
Lexus
1
"""

print()

a_2 = Auto()
a_2.on_auto_start("Mazda", "CX 9", 2018)
print(a_2.auto_name)
print(a_2.auto_count)

"""
Автомобиль заведен
Mazda
2
"""
