# 32). Задайте последовательность чисел. Напишите программу, которая выведет
#  список неповторяющихся элементов исходной последовательности.
import os
os.system('cls')


lst = [1,2,1,2,3,4]  #1 = 2 раза 2 = 2 раза 3.4 = 1 раз, следовательно нужен вывод [3,4]
print(lst)
lst_repeat = []

for i in lst:
    count=0
    for j in lst:
        if j == i:
            count+=1
    if count==1:
        lst_repeat.append(i)
            
print(lst_repeat)
