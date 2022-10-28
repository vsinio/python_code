# 1
def summ_digits(x):
    summ = 0
    while x != 0:
        summ += x % 10
        x = x // 10
    return summ


# 2
def delete_word(text, del_symb):
    """функция принимает исходный текст и элемент для удаления, далее создает список
    в который добавляются элементы не имеющие del_symb - элементов которые удаляются"""
    new_lst = text.split()
    lst_1 = []
    for i in new_lst:
        if del_symb not in i:
            lst_1.append(i)
    new_lst = ' '.join(lst_1)
    return new_lst


# 3 and 4
"""алгоритм сжатия и 'разжатия'"""
MESSAGE = "AAAAAAAAAAAAAABBBBBCDDDDDEEEEEF"


def first_rle(string):  # Функция RLE RESULLT: 14A5B1C5D5E1F
    """функция принимает строку, в процессе проходит каждый элемент сравнивая
    его с цифрой, если нет, то берет первую букву и умножает на счетчик"""
    final_str = ""
    counter = 1

    for index in range(0, len(string)):
        try:
            if string[index] == string[index + 1]:
                counter += 1
            else:
                final_str += str(counter) + string[index]
                counter = 1

            index += 1
        except IndexError:
            final_str += str(counter) + string[index]
    return final_str


def sec_rle(string):
    """Декодер"""
    final_str = ""
    index = 0
    count = ""
    for el in string:
        if el.isdigit():
            count += el
        else:
            final_str += int(count) * el
            count = ""
        index += 1
    return final_str


# 5
def from10to2(x):
    two_cc = ''
    while x > 0:
        cc = x % 2
        two_cc += str(cc)
        x //= 2
    return two_cc[::-1]

#6
def lst_keyboard(x):  # создать список от -N до N
    len_n = -x
    lst = []
    for i in range(x * 2 + 1):
        lst.append(len_n)
        len_n += 1

    return lst

#7
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-2) + fibonacci(n-1)

#8
def even_fn(x):
    if x % 2 == 0:
        return True
    return False
#9 odd
def odd(x):
    if x % 2 != 0:
        return True
    return False
#sec var fibbo
def secfibonacci(n): #фибоначчи второй вариант
    if n < 2:
        return n
    return secfibonacci(n-2) + secfibonacci(n-1)