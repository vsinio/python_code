# def f(x):
#     x**2
# g = f
# print(type(f))
# print(type(g))

# def f(x):
#     return x**2
# g = f

# print(type(f))
# print(type(g))

# # print(f(4))
# # print(g(4))

# def calc1(x):
#     return x+10

# # print(calc1(10))

# def calc2(x):
#     return x*10

# # print(calc2(10))

# def math(op,x):
#     print(op(x))

# math(calc2,10)
# math(calc1,10)

# _______________________

# def sum(x,y):
#     return x+y #снизу лямбда все то же самое!

# sum = lambda x,y: x+y+2

# def mylt(x,y):
#     return x*y

# def calc(op, a, b):
#     print(op(a,b))
#     # return op(a,b)

# calc(sum,4,5)

# calc(lambda x,y: x+y+2, 4,5)

# list = []
# for i in range(1,11):
#     # if(i%2 == 0):
#     list.append(i)
# print(list)

# def f(x):
#     return x**3

# lss = [(i,f(i))  for i in range(1,11) if i%2 == 0]
# print(lss)

lst = [1,2,3,5,8,15,23,38]
f = lambda x,y: x**y
lst_1 = [(i, f(i,2)) for i in lst if i%2==0]

print(lst_1)
