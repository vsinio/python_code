import subprocess
import chardet

ARG_1 = ['ping', 'yandex.ru']
ARG_2 = ['ping', 'youtube.com']

def PING_CALL(lst):
    ARG_PING = subprocess.Popen(lst, stdout=subprocess.PIPE)
    for i in ARG_PING.stdout:
        result = chardet.detect(i)
        line = i.decode(result['encoding'])
        print(line)
    print(result)

PING_CALL(ARG_1)
PING_CALL(ARG_2)


"""
Задание 5.

Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
преобразовать результаты из байтовового в строковый тип на кириллице.

Подсказки:
--- используйте модуль chardet, иначе задание не засчитается!!!
"""
