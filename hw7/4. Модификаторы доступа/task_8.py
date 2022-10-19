class MyClass:
    _attr = "значение"
    def _method(self):
        print("Это защищенный метод!")


mc = MyClass()
mc._method()
print(mc._attr)

"""
Это защищенный метод!
значение
"""
