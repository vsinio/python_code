"""Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
# 1 способ
#TO DO
text_for_def = "Арава арива братец барашка бред брат вот вон вид абва абв"
symb = ('а','б', 'в')
def del_symb(text, what_del):
    new_text = ""
    for i in text:
        if i not in what_del:
            new_text+=i
    return new_text
new_text = del_symb(text_for_def,symb)
print(new_text)

1st VAR"""

TEXT = "абвесили меня сегодня абвечером абв ноабве"
DEL_SYMB = "абв"
print(TEXT.split())

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

print(delete_word(TEXT, DEL_SYMB))

#2 VAR

TEXT_1 = "абвесили меня сегодня абвечером абв ноабве"
DEL_SYMB_1 = "абв"
print(TEXT.split())

LST = [el for el in TEXT_1.split() if DEL_SYMB_1 not in el]
LST = ' '.join(LST)

print(LST)