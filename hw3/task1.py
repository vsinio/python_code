# 22. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

from random import randint

len_lst = int(input("Введите длинну списка: "))
lst = []
for i in range(len_lst):
    lst.append(randint(0, 10))

print(f"список состоящий из {len_lst} элементов {lst}")


odd_summ = 0
index = 0
while index < len(lst):
    if index % 2 == 0:
        odd_summ += lst[index]
    index += 1

print(f"\while\сумма нечетных элементов = {odd_summ}")

odd_summ_2 = 0
for i in range(0,len_lst,2):
    odd_summ_2+=lst[i]

print(f"\For\сумма нечетных элементов = {odd_summ_2}")