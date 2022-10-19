class Auto:
    def on_start(self):
        info = "Автомобиль заведен"
        return info


a = Auto()
print(a.on_start())  # -> AttributeError: 'Auto' object has no attribute 'info'
