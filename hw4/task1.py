# 30). Вычислить число π c заданной точностью d
# Пример:
# при d = 0.001,π = 3.141 10^(-1)≤d≤10^(-10)
import os
os.system('cls')

from math import pi

accuracy = input(f"Введите необходимую точность от {10**(-1)} до {10**(-10)} \nв формате: 0.01, 0.001, 0.001 и тд.: \n")
dig_pi = str(pi)
print(dig_pi[0:len(accuracy)])