# 1st method

colors = ['red', 'green', 'blue']
data = open('file.txt','a') #'a' - добавляет все время данные в файл file.txt / 'w' заменяет все что есть и
# добавляет то, что написано свыше
data.writelines(colors)
data.write('\nLine1\n') #написать еще одно сообщение + на след стркоу
data.close()  #закрыть работу файла(оборвать связь)


# #2nd method
# with open('file.txt','w') as data:
#     data.write('line1\n')
#     data.write('line2\n')


# чтение данных

# path = 'file.txt'
# data = open(path, 'r') #'r' = чтение файлов
# for line in data:
#     print(line)
# data.close()

# exit()

# import lec2import as lec2 #as lec2 (использовать вместо полного названия файла)
# # импорт файла чтобы взять функции(можно делать библиотеки)
# print(lec2.summ_digits(55))

# немного функций

# def new_string(symbol, count=3): #если установить count=3<
#     #то 3 будет по дефолту, т.е. если не будет задано значение
#     return print(symbol*count)
# new_string('?', 10)
# new_string('!')

# def concatenatio(*params): # сколько угодно параметров(конкатенация)
#     #если поменять стр на инт и написать res : int = 0, то можно складывать числа
#     res: str = ''
#     for item in params:
#         res+=item
#     return res
# print(concatenatio('a','b','c'))


# кортеж - неизменяемый список TUPLE


# a = (3,4,5,6)
# print(a)
# print(type(a))
# print(f"a[2] = {a[2]}, a[-2] = {a[-2]}")


# СЛОВАРИ ( коллекция обьектов с доступом по ключу(KEYS))

# dictionary = {}

# dictionary = \
#     {
#         'up': 'to the top',
#         'left': '<<===',
#         'down': 'to the floor',
#         'right': '===>>'
#     }
# print(dictionary)
# print(dictionary['up']) #обращение к ключу

# print(dictionary.keys()) #показать ключи
# print(dictionary.values()) #показать значения ключей
# for k in dictionary.keys():
#     print(k) #показать ключи тоже

#множества

# colors = {'red', 'green', 'blue'}
# print(type(colors)) #class set

# colors.add('red')
# print(colors) #red green blue тк red уже есть
# colors.add('grey') # red green blue gray
# colors.remove('red') #=> green blue gray
# colors.remove('red') #error t.k. red уже удален и его нет
# colors.discard('red') #ok, поф что red нет, ошибка не будет. но если ред есть - удалит
# colors.clear() # очистит множество {}


# a = {1,2,3,4,5}
# b = {2,3,4,5,6,7,8}
# c = a.copy() #c = {1,2,3,4,5}
# u = a.union(b) # u = {1,2,3,4,5,6,7,8} - обьединение общих
# i = a.intersection(b) #пересечение 2,3,4,5}
# dl = a.difference(b) #что есть в а чего нет в б

#s = frozenset(a) #можно сделать фрозенсет(множество без удаления добавления и тд) как кортеж tuple

# lst1 = [1,2,3,4,5] при копии таким образом при изменении элементов 
#элементы меняются везде!
# lst2 = lst1
# lst1[0] = 123
# lst2[1] = 111
# for e in lst1:
#     print(e)
# print()
# for j in lst2:
#     print(j)

# lst = [1,2,3,4,5]
# print(len(lst))
# print(lst.pop()) #удаляет последний символ
# print(lst)
# print(lst.pop(2)) #удаляет второй символ(2 по индексу, тут это 3 !)
# print(lst)
# print(lst.insert(2,333)) # на элемент с индексом 2 вставляет число 333
# print(lst)
# lst.append(11) #добавляет 11 в конец 
# print(lst)

