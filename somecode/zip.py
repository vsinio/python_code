# func ZIP  для указаных итер обьектов выполняет перебор указанных переменных до окончания самого короткого из них

a = [1, 2, 3, 4]
b = [5, 6, 7, 8, 9, 10]
c = "python"

z = zip(a, b, c)
# print(z)
# print(next(z)) #1
# print(next(z)) #2
# print(next(z)) #3
# print(next(z)) #4
for x in z:
    print(x)
    # (1, 5)
    # (2, 6)
    # (3, 7)
    # (4, 8)
z = tuple(zip(a, b))  # ((1, 5), (2, 6), (3, 7), (4, 8))
print(z)

z = zip(a, b, c)  # распаковка
for v1, v2, v3 in z:
    print(v1, v2, v3)

z1, z2, z3, z4 = zip(a, b, c)  # распаковка
print(z1, z2, z3, z4)


