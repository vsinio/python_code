import os  # ОЧИСТИТЬ КОНСОЛЬ
from random import randint

os.system("cls")
print()
def new_random_lst(x):  # ввод количества элементов в списке
    from random import randint
    len_lst = x
    lst = []
    for i in range(len_lst):
        lst.append(randint(0, 10))
    return lst
lst = new_random_lst(6)
print(lst)
#          элемент     цикл за н    range() либо lst и тд.
nums = [randint(0,10) for n in range(0,6)] #lch список с рандомными числами
print(nums)


def from10to2(x): #перевод из 10 в 2 СС
    two_cc = ''
    while x > 0:
        cc = x % 2
        digit = str(cc)
        two_cc += digit
        x //= 2
    return two_cc[::-1] #переворот строки
print(from10to2(11))

def fibonacci(n): #фибоначчи рекурсия
    if n in (1, 2):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)
 
def secfibonacci(n): #фибоначчи второй вариант
    if n < 2:
        return n
    return secfibonacci(n-2) + secfibonacci(n-1)


print(fibonacci(5))


print("____")

#удалить повтор элементы
lst = [1,2,3,4,5,6,1,2,3]
def sort_rem(lst):
    uniq_el = set()
    for el in lst:
        if el not in uniq_el:
            uniq_el.add(el)
        else:
            uniq_el.discard(el)
    s = list(uniq_el)
    s.sort()
    return s
print(sort_rem(lst))
print(list(filter(lambda i: lst.count(i) ==1, lst)))
