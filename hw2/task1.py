# 14.	Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
#   Пример:
#	6782 -> 23
#	0,56 -> 11

a = float(input("Введите любое вещественное число: "))


def summ_digits(x):
    summ = 0
    while x != 0:
        summ += x % 10
        x = x // 10
    return summ


if a % 1 == 0:
    print(round(summ_digits(a)))
else:
    while a % 1 != 0:
        a *= 10
    print(round(summ_digits(a)))