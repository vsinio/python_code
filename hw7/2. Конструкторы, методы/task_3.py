class Auto:
    # атрибуты класса
    auto_count = 0

    # методы класса
    def __init__(self):
        self.auto_count += 1
        print(self.auto_count)

    def __add__(self, other):
        return self.auto_count + other.auto_count

    def __mul__(self, other):
        return self.auto_count * other.auto_count



a_1 = Auto()
a_2 = Auto()
a_3 = Auto()
print(a_1 + a_2)
print(a_1 * a_2)

"""
1
2
3
"""
