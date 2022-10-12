# 31). Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# 70 = 2*5*7 => [2, 5, 7]
# 140 = 2*2*5*7 => [2, 2, 5, 7]
# 140|2
# 70|2
# 35|5
# 7|7
import os
os.system('cls')

num = int(input("Введите натуральное число: "))
divider = 2
lst = []

while num !=1:
    if num%divider==0:  
        lst.append(divider)
        num=num//divider
    else:
        divider+=1

print(f"список множителей = {lst}")
