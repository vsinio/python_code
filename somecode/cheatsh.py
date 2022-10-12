"""
Проведение сравнительных замеров
"""
import time

def check_1(n):
    """
    Фиксируем отсечки времени до и после выполнения основной логики
    :param n:
    :return: кортеж из результата ф-ции и затраченного времени
    """

    start_val = time.time()
    res = 0

    for i in range(1, n + 1):
        res = res + i

    end_val = time.time()
    return res, end_val - start_val

print(check_1(3))