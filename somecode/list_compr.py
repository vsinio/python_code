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

d_inp = input("Введите целые числа через пробел: ") # получаем список
a = [int(d) for d in d_inp.split()] #инт преобразует str в int
print(a)


