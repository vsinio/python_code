# 25. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# o 45 -> 101101
# o 3 -> 11
# o 2 -> 10
#1 способ
cc = int(input("Введите число для перевода из 10 в 2 сс: "))
print(bin(cc))

#2 способ

def from10to2 (x):
    two_cc = ''
    while x > 0:
        cc = x%2
        two_cc+=str(cc)
        x//=2
    return two_cc
print(from10to2(cc))