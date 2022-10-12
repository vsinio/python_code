# # path = "/Users/marke/Desktop/myRepo/pythonpart1/pythonslection/lec3/file.txt"
# # f = open(path,"r")
# # data = f.read() + " " #считываем все что есть и добавляем пробел
# # f.close()

# # numbers = []
# # while data != " ":
# #     space_pos = data.index(" ")
# #     numbers.append(int(data[:space_pos]))
# #     data = data[space_pos+1:]
# # out = []
# # for e in numbers:
# #     if not e % 2:
# #         out.append((e,e**2))
# # print(out)


# data = '1 2 3 5 8 15 23 38'.split() #сделать список из строк

# res = list(map(int, data)) #сделать из строк списка -список из чисел
# res = filter(lambda x: not x%2, res)
# res = list(map(lambda x:(x, x**2), res))
# print(res)


# li = [x for x in range(1,20)]
# print(li)

# li = list(map(lambda x:x+10, li))
# print(li)

## data = list(map(int,input().split()))
## print(data)

# data = [x for x in range(10)]
# res = list(filter(lambda x: not x%2, data))
# print(res)


lst_name = ['user1','user2','user3','user4']
salary = [111,222,333,444]
main = list(zip(lst_name,salary))
print(main) #если 1 из список меньше, то колво в зипе будет = меньшему размеру списк

data = list(enumerate(lst_name))
print(data)