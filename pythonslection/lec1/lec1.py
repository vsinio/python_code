# #print("hello world")
#
# #a = 2
# #b = 3.23
# #c = "Hello"
# #d = None
# #f = True
#
# #lst_a = [1,2,3] #список (int str и тд)
# #print(a, (type(a))) #type(переменная) функция показывающая класс (int)
# #print(b, (type(b))) float
# #print(c, (type(c))) str
# #print(d, (type(d))) none
# #print(f, (type(f))) bool
# #print(a,'-',b,'-',c)
# #print('{0} - {1} - {2}'.format(a,b,c))  #применение форматированной строки, все по порядку(по индексам)
# #print(f'{a} - {b} - {c}') #f строка
# #print(f, (type(f)))
# #print(lst_a)
#
#
# #print("press a")
# #a = int(input()) # input = always str, if u need int - a = int(input()), float - float(input())
# #print('press b')
# #b = int(input())
# #print(f'a = {a}, b = {b}')
# #c = a + b
# #print(a, '+', b, '=', a+b)
# #print(a, '+', b, '=', c)
# #print(a+b)
#
#
# # + - / // % * **
# """a = 15
# b = 4
# print(type(a/b)); print(a/b) #обычное деление(инты может во флот превратить)
# print(a//4) #целочисленное деление (15 / 4 = 3)
# print(a%b) #остаток от деления 15 % 4 = 3
# print(a**b) #** = возведение в степень = 15^4"""
#
# """a = 1.333
# b = 3
# c = (a * b)
# print(c) # 3.900000000004 ~ поэтому надо делать округление, round
# #round по дефолту округляет к целым числам, пример: (в скобках указываем колво необходимых знаков (всего))
# c = round(a*b, 3)
# print(c) # = 4 """
#
# '''a = 3
# a +=5 #a =  a + 5 аналогично и для других операций
# print(a)'''
#
# '''a = 1 > 4
# print(a) # 1 > 4 = False, etc
# a = 1 < 4 and 3 > 5
# print(a)
# a = 1 == 2
# print(a)
# a = 1 != 4
# print(a)
#
# b = [1,2]
# c = [1,2]
# print(b == c) # True тк сравнение идет по элементно'''
#
# #func = 1
# #T = 4
# #x = 123
#
# #print(func<T>x)
#
# #f = 1 > 2 or 4 < 6 # тк 1 истинно = True
# #f = [1,2,3,4]
# #print(2 in f) # тк 2 есть в списке f = True
# #f = [1,2,3,4]
# #print(not 2 in f) # тк 2 есть в списке f = False
#
# '''f = [1,2,3,4]
#
# is_odd = not f[1] % 2  #is_odd = f[1] % 2 == 0 /// true тк f[1] (индекс) = 2
# print(is_odd) '''
#
# # if else   обязательно после if else ставить :
#
# '''a = int(input())
# b = int(input())
# if a>b:
#     print(f'большее число : {a}')
# else:
#     print(f'большее число : {b}')'''
#
# '''username = input('Введите имя пользователя: ')
# if username == 'Masha':
#     print("Hello Masha")
# elif username == 'Vanya':
#     print('Hello Sin')
# elif username == 'Sasha':
#     print('Hello Alex')
# else:
#     print('Знакомы?')'''
#
# #while и после двоеточие!!!
#
# '''origin = 233
# invert = 0
# while origin != 0:
#     invert = invert * 10 + ( origin % 10)
#     origin //=10
# else:
#     print('Пожалуй')
#     print('Хватит')
# print(invert)    '''
#
# #цикл for
#
#
# '''lst = [32,2235,337,332,142]
# for i in lst:
#     print(i)
# r = range(10) # создание от 0 до 10(не вкл) 0 1 2 3 4 5 6 7 8 9
# k = range(1,5) # от 1 вкл до 5 не вкл, т.е. 1,2,3,4
# m = range(1,10,2) # от 1 вкл до 10 не вкл с шагом 2! т.е. 1 3 5 7 9
# for i in k:
#     print(i)'''
#
#     # немного о строках
#
# '''text = 'сьешь еще этих мягких французских булок'
# print(len(text)) # длина строки
# print('еще' in text) # проверка 'еще' в переменной text = true
# print(text.isdigit()) # проверка являются ли все символы числами false
# print(text.islower()) # являются ли все в нижнем регистре БеЗ ВоТТ этОгО true
# print(text.replace('еще', 'ЕЩЕ')) #замена маленького еще на большое ЕЩЕ
# #срезы
# print(text[1]) #ь тк индекс
# print(text[:]) #все, тк от 0 до len(text)-1
# print(text[::6]) #сеикакл, тк от 0 до конца каждые 6 символов
# print(text[:5]) #сьешь тк от 0 до индекса5 не вкл(0.1.2.3.4)
# print(text[-5])#б   отсчет с конца'''
#
# #списки
#
# '''numbers = [1,2,3,4,5]
# ran = range(1,6) #1,2,3,4,5
# numbers1 = list(ran)
# print(numbers)
# print(numbers1)'''
#
# '''col = ['red', 'green', 'blue']
# print(col) #r g b
# col.append('gray')#добавить в конец списка
# print(col)#r g b gray
# print(col*2)#r g b r g b
# print()
# for i in col:
#     print(i*2) #вывод элементов из цикла: rr, gg, bb, grgr
# print()
# col.remove('red') #удалить элемент red из списка col[0] = так же можно по индексу
# #так же можно del[0]
# print(col)
# del col[1] #удалить жлемент блу
# print(col)
# '''
#
# '''#функции
# def f(x):
#     if x==1:
#         return "целое" #str
#     elif x == 2.3:
#         return 23 #int
#     else:
#         return #nonetype
#
# print(f(255))'''