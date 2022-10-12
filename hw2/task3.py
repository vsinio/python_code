#16). Задайте список из n чисел последовательности 〖(1+1/n)〗^n и выведите на экран их сумму.

n  = int(input("Введите N: "))
lst = []
summ_digits = 0
index = 0

for i in range(1,n+1):
    lst.append(pow(1+1/i, i))

while index != len(lst):
    summ_digits+=lst[index]
    index+=1
    
print(f"список чисел = {lst}")
print(f"сумма чисел из списка = {summ_digits}")
