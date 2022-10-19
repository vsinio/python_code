class MyClass:
    __attr = "значение"
    def __method(self):
        print("Это защищенный метод!")


mc = MyClass()
mc._MyClass__method()
print(mc._MyClass__attr)

"""
Это защищенный метод!
значение
"""
