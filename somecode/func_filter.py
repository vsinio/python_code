# func filter
# фильтрация элементов итерированного обьекта

# filter(func, *iterables) если func == true, то фильтрует и возвращает, если нет - нет

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

b = filter(lambda x: x % 2 == 0, a)
print(b)  # так же можно пройтись по фильтру через next(b)
# for x in b:
#     print(x)
lst = tuple(b)  # (2, 4, 6, 8, 10) list и тд
print(lst)  #


def if_prost(x):
    d = x - 1
    if d < 0:
        return False
    while d > 1:
        if x % d == 0:
            return False
        d -= 1
    return True


a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(filter(if_prost, a)))  # вывод списка + фильтрация по функции, список

lst = ['Москва', 'Рязань1', 'Смоленск', 'Тверь2', 'Томск', 'Москва4']

b = filter(str.isalpha, lst)  # вывод только если все символы буквы
print(list(b))

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = filter(if_prost, a)  # [1, 2, 3, 5, 7] простые числа
b2 = filter(lambda s: s % 2 != 0, b)  # нечетные простые числа
print(list(b2))

#в одну строку можно код выше
b2 = filter(lambda s: s % 2 != 0, filter(if_prost, a))
print(f"{list(b2)} в одну строку")