# 34). Даны два файла, в каждом из которых находится запись многочлена, приравненного к нулю. 
# Задача - сформировать файл, содержащий сумму многочленов (суммируем подобные слагаемые).
# Пример:
# 1 Файл : 2*x2 + 4*x + 5 = 0
# 2 Файл : 4*x2 + 7*x + 9 = 0
# 3 Файл: (содержит результат) 6*x2 + 11*x + 14 = 0

def read_file(name):
    path = str(name)
    data = open(path, 'r') #'r' = чтение файлов
    for line in data:
        pass #1 None => pass
    data.close()
    return str(line)


f_file = read_file('file1.txt')
sec_file = read_file('file2.txt')

print(f_file)
print(sec_file)

def newdig_lst(x):
    lst = []
    for i in x:
        if i.isdigit(): #2 ==TRUE delete
            lst.append(i)

    return lst

lst_1 = newdig_lst(f_file)
lst_2 = newdig_lst(sec_file)

def summ_lst(x,y): #сумма двух списков цифр полученных из файлов 
    lst = [1,2,3,4,5,6,7]
    summa = 0
    while summa != len(x):
        lst[summa] = int(x[summa])+int(y[summa])
        summa+=1
    lst[1]=lst[1]//2 #степень первого
    lst[3]=lst[3]//2 #степень второго

    return lst
bc = summ_lst(lst_1, lst_2)
summ_polynomial = f"{bc[0]}x^{bc[1]} + {bc[2]}x^{bc[3]} + {bc[4]}x + {bc[5]} = {bc[6]}" #3 ()

with open(f"file_summ.txt","w") as data:
    data.write(summ_polynomial)




print("Сумма двух многочленов")
print(summ_polynomial)
#печать многочлена


# a = "5"
# a1 = str(5)
# print(a.isdigit())
# print(a1.isdigit())


