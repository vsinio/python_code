# 33). Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) 
# многочлена и записать в файл многочлен степени k и приравняйте его к нулю.
# Пример:
# k=2 => 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
# 2*x*2 + 4*x + 5 = 0
# или
# 2*x^2 + 4*x + 5 = 0
from random import randint

x = int(input("Введите К: "))

def polynomial(x):
    s = ''
    copy_x = x
    while copy_x > -1:
        
        if copy_x == 1:
            s = s + (f"{randint(1,9)}x + ")

        elif copy_x==0:    
            s = s + (f"{randint(1,9)} = 0")
        elif copy_x > 1:
            s = s + (f"{randint(1,9)}x^{copy_x} + ")
        copy_x-=1

    return str(s)
    
print(polynomial(x))

def new_file(x):
    for i in range(2):
        with open(f"file{i+1}.txt","w") as data:
            data.write(polynomial(x))

new_file(x)

# {
    # from random import randint
# def Mnogochlen_in_Stepen_K(k):  # Функция построения уравнения типа 2x² + 4x + 5 = 0 для к-ой степени возвращает строку с уравнением
#     Stroka=''
#     Okonchnie = ''
#     Mnozitel = '*'
#     for i in range(k,-1,-1):                    # Перебираем все порядки до степени от к до 0
#         Coeficient = randint(0,10)               # Генерируем коэфициент
#         if Coeficient == 0:                       # Проверка наличия коэфициента т.е. Coeficient  равен 0
#             STR_Coeficient = ''                     # мы не вставляем в сроку элементы подобные +2*x^к-1 или 4*x^к
#             Stepen = ''
#         else:                                   #  Coeficient не равен 0
#             if Coeficient == 1:                     #  Coeficient не равен 1 то исключаем запись 1*x^к преобразуя её в x^к
#                 STR_Coeficient = ''
#                 Mnozitel = ''
#             else:
#                 STR_Coeficient =str(Coeficient) #  Coeficient больше 1 создаем запись типа  Coeficient*x^к
#                 Mnozitel = '*'

#             if i == 1:                  # Проверка степени Stepen = 1 то запись выглядит как х вместо x^1
#                 Stepen = STR_Coeficient + Mnozitel+'x'
#             else:
#                 Stepen = STR_Coeficient + Mnozitel+'x^'+str(i)    # Stepen > 1 то строится запись вида *x^Stepen

    
#         if i == 0:               # Проверка степени Stepen = 0 то запись выглядит как 4 вместо 4*x^0 
#             if Stroka == '': Stroka = 'x'
#             Okonchnie = ' = 0'       # добавляется окончание = 0 заканчивающее уравнение
#             Stepen = STR_Coeficient

#         if  Stepen == '' or Stroka == '':  # проверка на добавление знака + в уравнение для этого перед ним чтото должно быть и за ним должна быть запись не равная 0
#             Plus = ''                                        
#         else:
#             Plus =' + '
#         Stroka += Plus  + Stepen + Okonchnie #склеивание операндов и добавление в строку
#     return Stroka

# Imput_error = True 
# while Imput_error:                                      # Запрашиваем ввод степени многочлена уравнения с проверкой правильности введенных данных
#     str1 = input('Введите степень многочлена к = ')
#     try:
#         k = int(str1)
#         if k < 0:
#             print('Введите положительное число    ')
#             Imput_error = True
#         else:
#             Imput_error = False       
#     except ValueError:
#         print("Это не правильный ввод, попоробуйте снова")



# Imput_error = True 
# while Imput_error:                                          # Запрашиваем ввод колличества создаваемых файлов с проверкой правильности введенных данных
#     str1 = input('Введите колличество создаваемых файлов N >=1 ')
#     try:
#         N = int(str1)
#         if N < 0:
#             print('Введите число более 0   ')
#             Imput_error = True
#         else:
#             Imput_error = False       
#     except ValueError:
#         print("Это не правильный ввод, попоробуйте снова")

# for i in range(N):                      # цикл по созданию файлов
#     file_Name = 'file' + str(i) + '.txt'    # генерируем название создаваемого файла
#     file = open(file_Name,'w')               # создаем или открываем новый файл
#     Stroka = Mnogochlen_in_Stepen_K(k)        # генерируем строковую переменную с необходимым уравнением с заданной степенью
#     file.write(Stroka)                      # записываем данную строку в файл
#     file.close                          #заканчиваем работу с файлом
#     print(f'В файл и именем {file_Name} записана строка: ',Stroka)       #вывод строки на экран
#}