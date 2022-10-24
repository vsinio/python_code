"""
Задание 1.
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init()__),
который должен принимать данные (список списков) для формирования матрицы.
[[], [], []]
Следующий шаг — реализовать перегрузку метода __str()__ для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add()__ для реализации операции
сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно —
первый элемент первой строки первой матрицы складываем
с первым элементом первой строки второй матрицы и т.д.
Пример:
1 2 3
4 5 6
7 8 9
1 2 3
4 5 6
7 8 9
Сумма матриц:
2 4 6
8 10 12
14 16 18
"""


class Matrix:
    """класс содержащий в себе список с 3 списками(элементы матрицы)"""

    def __init__(self, lst=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]):
        self.lst = lst

    def __str__(self):
        return f"{' '.join(map(str, self.lst[0]))}\n{' '.join(map(str, self.lst[1]))}" \
               f"\n{' '.join(map(str, self.lst[2]))}"

    def __add__(self, other):
        el_1 = [x + y for x, y in zip(self.lst[0], other.lst[0])]
        el_2 = [x + y for x, y in zip(self.lst[1], other.lst[1])]
        el_3 = [x + y for x, y in zip(self.lst[2], other.lst[2])]
        lst_summ = [el_1, el_2, el_3]
        return Matrix(lst_summ)


mat_1 = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
mat_2 = [[3, 3, 3], [2, 2, 2], [1, 1, 1]]

m1 = Matrix(mat_1)
m2 = Matrix(mat_2)

print(m1 + m2)
