class Auto:
    def __init__(self):
        self.auto_name = "Mazda"  # публичный тип
        self._auto_year = 2019  # _ (1) - protected защищенн / _ - скорее всего заметка для служебного пользования
        #_ нужен для работы в классах
        self.__auto_model = "CX9"  # __ - private / __ - вызвать нельзя - доступен внутри класса


a = Auto()
print(a.auto_name)  # -> Mazda
print(a.auto_model)  # -> AttributeError: 'Auto' object has no attribute 'auto_model'
