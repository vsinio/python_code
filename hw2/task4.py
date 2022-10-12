#	17). 1. Задайте число N, создайте список: [-N, N].
# 3. Найдите произведение элементов на указанных позициях.
# 2. Позиции (случайные) хранятся в файле file.txt (создаётся во время выполнения кода и зависит от
# количества элементов в списке) в одной строке одно число.
# Пример:
# Файл:
# 4
# 5
# 2
# N = 3 => [-3, -2, -1, 0, 1, 2, 3]
#Результат: 1*2*(-1) = -2
from random import randint

a = int(input("Введите число N: "))  # ввод числа
reverse_a = -a
lst = []
while reverse_a != a+1:
    if a <= 0:
        print("Число меньше либо = 0")
        break
    lst.append(reverse_a)
    reverse_a += 1
print(f"Список от -{a} до {a} = {lst}")  # отображение списка от -н до н

# создание списка с рандомными индексами
lst_random_index = [randint(0, 2*a), randint(0, 2*a), randint(0, 2*a)]
# преобразование из инт в стр для записи в файл
lst_random_index_string = list(map(str, lst_random_index))
# создание файла и включение в него рандомных индексов для перемножения
with open(r'C:\Users\marke\Desktop\myRepo\pythonpart1\hw2\task4.txt', 'w') as data:
    for line in lst_random_index_string:
        data.write(line + '\n')

print(
    f"Список рандомных индексов = {lst_random_index} \n p.s. индексы записаны в task4.txt в этой же папке")
# вывод результата

result = lst[lst_random_index[0]] * \
    lst[lst_random_index[1]] * lst[lst_random_index[2]]
print(
    f"результат программы {lst[lst_random_index[0]]} * {lst[lst_random_index[1]]} * {lst[lst_random_index[2]]} = {result}")
