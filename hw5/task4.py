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


print(first_rle(MESSAGE))

MESS_RES = "14A5B1C5D5E1F"


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


print(sec_rle(MESS_RES))
