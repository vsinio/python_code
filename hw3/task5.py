# 26. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
#  для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
# (-1)**(x+1) * fibonacci(x)
import os
os.system('cls')

def lst_keyboard(x):  # создать список от -N до N
    len_n = -x
    lst = []
    for i in range(x*2+1):
        lst.append(len_n)
        len_n+=1
        
    return lst
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-2) + fibonacci(n-1)

    



N = int(input("Введите N: "))
lst = lst_keyboard(N)
lst_fibb = []
lst_mines_fibb = []

for i in lst:
    if lst[i] > 0:
        lst_fibb.append(fibonacci(lst[i]))
    elif lst[i] == 0:
        lst_fibb.insert(0,0)
    else:
        lst_mines_fibb.append(((-1)**(i+1)) * fibonacci(abs(lst[i])))
        


print(f"Первоначальный список = {lst}")
print(f"Список с числами Фибоначчи 0+= = {lst_fibb}")
print(f"Список с числами Фибоначчи 0- = {lst_mines_fibb}")
print(f"Итоговый список с числами Фибоначчи = {lst_mines_fibb + lst_fibb}")