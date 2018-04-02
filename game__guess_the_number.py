#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'ipetrash'


"""
Угадай число

Компьютер загадывает число в диапазоне от 1 до N.
Игрок будет пытаться угадать его и если не угадывает, то компьютер подсказывает
больше или меньше введенное число загаданного компьютером.

"""


import random


while True:
    num = input('Введите максимальное значение диапазона N: ')

    if num.isdecimal():
        N = int(num)
        if N <= 0:
            print('Число должно быть больше 0')
            continue

        break

    else:
        print('Неправильный формат числа: "{}"\n'.format(num))


trying = N // 10
print('Количество попыток: {}\n'.format(trying))

hidden_num = random.randint(1, N)
print('Я загадал число "?"\n')

while True:
    num = input('Введите число: ')

    # TODO: Удалить
    if num == 'show':
        print(hidden_num)
        continue

    if not num.isdecimal():
        print('Неправильный формат числа: "{}"\n'.format(num))
        continue

    num = int(num)
    if num <= 0:
        print('Число должно быть больше 0')
        continue

    if num == hidden_num:
        print('Победа!')
        break

    elif num > hidden_num:
        print('Неа, "?" < "{}"'.format(num))

    else:
        print('Неа, "?" > "{}"'.format(num))

    trying -= 1

    if trying == 0:
        print('Закончились попытки. Проирыш!\nЗагаданное число: ' + hidden_num)
        break

    print('Осталось попыток: {}\n'.format(trying))
