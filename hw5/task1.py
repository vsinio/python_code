# # Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
# # 1 способ
# #TO DO
# text_for_def = "Арава арива братец барашка бред брат вот вон вид абва абв"
# symb = ('а','б', 'в')
# def del_symb(text, what_del):
#     new_text = ""
#     for i in text:
#         if i not in what_del:
#             new_text+=i
#     return new_text
# new_text = del_symb(text_for_def,symb)
# print(new_text)


text = "абвесили меня сегодня абвечером абв ноабве"
delete = "абв"


def delete_word(text, delete):
    lst = text.split()
    lst_1 = []
    for i in lst:
        if delete not in i:
            lst_1.append(i)
    new_lst = ' '.join(lst_1)
    return new_lst


print(delete_word(text, delete))
