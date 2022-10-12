MESSAGE = "AAAAAAAAAAAAAABBBBBCDDDDDEEEEEF"
def RLE(somestr):  # Функция RLE RESULLT: 5A5B1C5D5E
    final = ""
    counter = 1
    j = 0
    for i in somestr:

        if somestr[j] == somestr[j + 1]:
            counter += 1
        else:
            final += str(counter) + somestr[j]
            counter = 1

        j += 1
        if j == len(somestr) - 1:
            final += str(counter) + somestr[j]
            return final


print(RLE(MESSAGE))

# j+=1
# if j+1 == len(somestr):
# final+=str(counter)+somestr[j]

MESS_RES = "14A5B1C5D5E1F"


def res_RLE(somestr):  # decoder
    final_str = ""
    index = 0
    count = ""
    for i in somestr:
        if i.isdigit():
            count += i
        else:
            final_str += int(count) * i
            count = ""
        index += 1
    return final_str


print(res_RLE(MESS_RES))
