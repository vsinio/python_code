class Auto:
   info_1 = "Автомобиль заведен"

   def __init__(self, my_var):
       self.my_var = my_var

   def on_start(self):
       info_2 = "Автомобиль заведен"
       return info_2


a = Auto(1)
print(a.info_1)  # -> Автомобиль заведен
# сеттер
# дескрипторы - атрибуты со связанным поведением

a.info_1 = 1