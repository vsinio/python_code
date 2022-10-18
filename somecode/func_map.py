# Функция MAP - 1ый аргумент - функция, которая последовательно будет применяться к каждому
# итерируемому обьекту стоящем на втором аргументе
# b = map(int, ['1', '2', '3', '4', '5']) - int - функция, список - аргумент

b = map(int, ['1', '2', '3', '4', '5'])

print(b)  # <map object at 0x0000023E1A342140>
print(next(b))  # некст по очереди призывает результат функции map
print(next(b))
print(next(b))
# отображение списка
print("________")

b = list(map(int, ['1', '2', '3', '4', '5']))

print(b)  # [1, 2, 3, 4, 5]
c = map(int, ['1', '2', '3', '4', '5'])
a = list(c)
print(a)
print("________")

q = (int(x) for x in ['1', '2', '3', '4', '5'])
q = list(q)  # Генератор
print(q)

cities = ['moscow', 'tversk obl', 'tula', 'rzn']

city = map(len, cities)
cit = list(city)
print(cit)

city = map(str.upper, cities)
cit = list(city)
print(cit)


def symbols(s):
    return list(s.lower())


city = map(symbols, cities)
cit = list(city)
print(cit)

# ==

city = map(lambda s: list(s.lower()), cities)
cit = list(city)
print(cit)

city = map(lambda s: s[::-1], cities)
cit = list(city)
print(cit)

s = map(int, input().split())
a = list(s)
print(a)