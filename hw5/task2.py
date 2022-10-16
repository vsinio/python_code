from random import randint


def input_dat(name):
    """"функция запрашивает имя игрока, затем дает выбор игроку сколько конфет взять от 1 до 28"""
    candy_qty = int(input(f"{name}, введите количество конфет, которое возьмете от 1 до 28: "))
    while candy_qty < 1 or candy_qty > 28:
        candy_qty = int(input(f"{name}, введите корректное количество конфет: "))
    return candy_qty


def p_print(name, step, counter, edge_candys):
    """информацию по ходу, кто ходил, сколько взял, сколько сейчас и сколько осталось"""
    print(f"Ходил {name}, он взял {step}, теперь у него {counter}. Осталось на столе {edge_candys} конфет.")


player_first = input("Введите имя первого игрока: ")
player_second = input("Введите имя второго игрока: ")
ALL_CAND = 2021
RAND_POS = randint(0, 2)  # определение игрока
if RAND_POS:
    print(f"Первый ходит {player_first}")
else:
    print(f"Первый ходит {player_second}")

COUNT_FRST = 0
COUNT_SEC = 0

while ALL_CAND > 28:
    if RAND_POS:
        candy_takes = input_dat(player_first)
        COUNT_FRST += candy_takes
        ALL_CAND -= candy_takes
        RAND_POS = False
        p_print(player_first, candy_takes, COUNT_FRST, ALL_CAND)
    else:
        candy_takes = input_dat(player_second)
        COUNT_SEC += candy_takes
        ALL_CAND -= candy_takes
        RAND_POS = True
        p_print(player_second, candy_takes, COUNT_SEC, ALL_CAND)

if RAND_POS:
    print(f"Выиграл {player_first}")
else:
    print(f"Выиграл {player_second}")
