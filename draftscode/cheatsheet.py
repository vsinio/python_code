# Деление на ноль недопустимо
try:
    res = 100 / 0
except ZeroDivisionError:  # Exception на все случаи ошибок-
    print("На ноль делить нельзя")
else:
    (f"Все норм, результат {res}")
finally:
    print("Программа завершена")

f = lambda x: x + x
print(f(5))


def even_fn(x):
    if x % 2 == 0:
        return True
    return False

s = [1, 3, 2, 5, 20, 5, 6, 7, 8, 10, 21]
print(list(filter(even_fn, s)))
print(list(filter(lambda x: x % 2 == 0,s)))

# вывод: [2, 20]

# map() — это встроенная функция Python, принимающая в качестве аргумента функцию и последовательность.
# Она работает так, что применяет переданную функцию к каждому элементу.
#
# Предположим, есть список целых чисел, которые нужно возвести в квадрат с помощью map.

L = [1, 2, 3, 4]
print(list(map(lambda x: x**2, L)))
