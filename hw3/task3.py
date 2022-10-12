# 24. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу 
# между максимальным и минимальным значением дробной части элементов.
# Пример:
# o [1.1, 1.2, 3.1, 5, 10.01] => 0.19

def new_random_lst(x): #ввод количества элементов в списке
    from random import randint, uniform
    len_lst = x
    lst = []
    for i in range(len_lst):
        lst.append(round(uniform(1, 10),2)) #float числа с округлением до 3 знаков после запятой
    return lst

lst = new_random_lst(6)
lst_sec = []

for i in range(len(lst)): #наполнил список lst_sec дробными частями элементов из списка lst
    lst_sec.append(round(lst[i]%1,2))

print(f"\nПервоначальный список = {lst}\n")
print(f"Новый список с дробной частью = {lst_sec}\n")
print(f"max дробная часть = {max(lst_sec)} \n\nmin дробная часть = {min(lst_sec)}\n")
print(f"Вывод как в примере: \n\n{lst} => {round(max(lst_sec) - min(lst_sec),2)}")


