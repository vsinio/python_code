# класс Auto
class Auto:
    def auto_start(self, param_1, param_2=None):
        if param_2 is not None:
            print(param_1 + param_2)
        else:
            print(param_1)

class Car:
    def auto_start(self, param_1, param_2=None):
        pass

a = Auto()
c = Car()

lst = [a, c]
for el in lst:
    print(el.auto_start(1, 2))


a = Auto()
a.auto_start(50)
a = Auto()
a.auto_start(10, 20)

"""
50
30
"""

1 + 1
'a' + 'n'