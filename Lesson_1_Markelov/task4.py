def print_lst(lst):
    '''по-строчная печать списка'''
    for i in lst:
        print(i, type(i))


words = ['разработка', 'администрирование', 'protocol', 'standard']
words_in_bytes = []
words_new = []
counter = 0

for i in words:
    words_in_bytes.append(i.encode('utf-8'))
    words_new.append(words_in_bytes[counter].decode('utf-8'))
    counter += 1


print("первоначальный список:")
print_lst(words)
print("список в байтах:")
print_lst(words_in_bytes)
print("декодированный список(идентичный первому):")
print_lst(words_new)

"""
Задание 4.

Преобразовать слова «разработка», «администрирование», «protocol»,
«standard» из строкового представления в байтовое и выполнить
обратное преобразование (используя методы encode и decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
"""
