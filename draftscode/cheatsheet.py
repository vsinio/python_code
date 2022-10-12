# Деление на ноль недопустимо
try:
    res = 100/0
except ZeroDivisionError: #Exception на все случаи ошибок- 
    print("На ноль делить нельзя")
else:
    (f"Все норм, результат {res}")
finally:
    print("Программа завершена")
