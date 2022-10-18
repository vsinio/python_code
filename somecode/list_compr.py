# list compr
# список из 6 нулей
# 1 var
N = 6
a = [0] * N  # дублирование ( можно создать список и так )

for i in range(N):
    a[i] = i ** 2
print(a)
# 2 var
lst = []
for j in range(6):
    lst.append(j ** 2)
print(lst)

# lc var
# synt for lc lst = [что с переменной х for x in range(N)]
lst = [x ** 2 for x in range(N)]  # [обьект возврата далее цикл и то, с чем мы будем работаьь
print("list compr")
print(lst)
# else synt [<способ формирования значения> for <переменная> in <итерируемый обьект>]

lst_1 = [x % 4 for x in range(N + 1)]  # остатки при делении на 4
print(lst_1)

lst_2 = [x % 2 == 0 for x in range(N)]  # вычислить четные (true) и нечетные false)
print(lst_2)

lst_3 = [0.5 * x + 1 for x in range(N)]  # список с линейной функцией
print(lst_3)

print("_____")

# d_inp = input("Введите целые числа через пробел: ") # получаем список ("Введите целые числа через пробел: ")
# a = [int(d) for d in d_inp.split()] #инт преобразует str в int
# print(a)

b = [d for d in "python123"]  # так же можно работать со строкой [[ord(d) for d in "python123"]] список из кодов
print(b)
b = [d.isdigit() for d in "python1234"]  # проверка элементов на цифры
print(b)
b = [d for d in "python123" if d.isdigit()]  # проверка элементов на цифры
print(b)

t = ['eee', 'ooo', 'cool', 'python']
a = [len(d) for d in t]  # список из длинн элементов списка
print(a)

a = [x for x in range(-5, 6)]  # [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
print(a)
a = [x for x in range(-6, 7) if x % 2 == 0 and x % 3 == 0]  # условие пишется в конце, иф
print(a)

print("_____")
cities = ['moscow', 'tversk obl', 'tula', 'rzn']
a = [city for city in cities if len(city) < 5]  # длинна меньше 5
print(a)

d = [4, 3, -5, 0, 2, 11, 122, -8, 9]
a = ["четное" if x % 2 == 0 else "нечетное" for x in d]  # if else <> можно записать в первую строку
print(a)
a = ["четное" if x % 2 == 0 else "нечетное"  # a = ["четное" if x % 2 == 0 else "нечетное" for x in d if x>0]
     for x in d
     if x > 0]  # только для положительных значений
print(a)
