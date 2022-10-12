# 23. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# o [2, 3, 4, 5, 6] => [12, 15, 16];
# o [2, 3, 5, 6] => [12, 15]

from random import randint

len_lst = int(input("Введите длинну списка: "))
lst = []
lst_2 = []
for i in range(len_lst):
    lst.append(randint(0, 10))

print(lst)

index = 0
first_index = 0
last_index = -1
while index != len(lst) // 2:
    lst_2.append(lst[first_index]*lst[last_index])
    index += 1
    first_index += 1
    last_index -= 1
if len_lst % 2 == 1:
    lst_2.append(lst[len_lst//2]**2)

print(lst_2)
