MESSAGE = "AAAAAAAAAAAAAABBBBBCDDDDDEEEEEF"

def first_rle(string):  # Функция RLE RESULLT: 14A5B1C5D5E1F
    final_str = ""
    counter = 1

    for j in range(0, len(string)):
        try:
            if string[j] == string[j + 1]:
                counter += 1
            else:
                final_str += str(counter) + string[j]
                counter = 1

            j += 1
        except IndexError:
            final_str += str(counter) + string[j]
    return final_str



print(first_rle(MESSAGE))

MESS_RES = "14A5B1C5D5E1F"


def sec_rle(string):  # decoder
    final_str = ""
    index = 0
    count = ""
    for i in string:
        if i.isdigit():
            count += i
        else:
            final_str += int(count) * i
            count = ""
        index += 1
    return final_str


print(sec_rle(MESS_RES))
