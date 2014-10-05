# -*- coding: utf-8 -*-


__author__ = 'ipetrash'


# TODO: побольше примеров форматирования строк.
# https://docs.python.org/3/library/string.html#string-formatting
# print('{one} * {one} {two}'.format(one="45", two="Bugaga"))


# def my_func(value):
#     print()
#     print(isinstance(value, str))
#     print(isinstance(value, int))
#     print(isinstance(value, bool))
#     return value


# import re
# import os
# # file_name = input("File name: ")
# file_name = "D:\hosts.txt"
# if os.path.exists(file_name):
#     with open(file_name) as file:
#         for row in file:
#             m = re.search(r"(\d{1,3}).(\d{1,3}).(\d{1,3}).(\d{1,3})(/(\d{1,3}))?", row)
#             if m:
#                 ip = m.group(0)
#                 ip_1 = m.group(1)
#                 ip_2 = m.group(2)
#                 ip_3 = m.group(3)
#                 ip_4 = m.group(4)
#                 ip_5 = m.group(6)  # m.group(5) -- this (/([0-9]{1,3})), m.group(6) -- ([0-9]{1,3})
#                 if ip_5:
#                     print("ip: '{}':\n    1:'{}' 2:'{}' 3:'{}' 4:'{}' 5:'{}'".format(ip, ip_1, ip_2, ip_3, ip_4, ip_5))
#                 else:
#                     print("ip: '{}':\n    1:'{}' 2:'{}' 3:'{}' 4:'{}'".format(ip, ip_1, ip_2, ip_3, ip_4))
#                 print()


# # Overlay "watermark" image / Наложение "водяного знака" на изображение
# import os
# from PIL import Image, ImageDraw, ImageFont
#
# # from PIL import Image, ImageDraw
# # text = "Hello, PIL!!!"
# # color = (0, 0, 120)
# # img = Image.new('RGB', (100, 50), color)
# # imgDrawer = ImageDraw.Draw(img)
# # imgDrawer.text((10, 20), text)
# # img.save("pil-basic-example.png")
#
# path = r"C:\Users\ipetrash\Desktop\pic.png"
# # path = input("Input path: ")
# path = os.path.normpath(path)
# if os.path.exists(path):
#     print("File: %s" % path)
#
#     image = Image.open(path)
#     width, height = image.size
#     # image.show()
#
#     drawer = ImageDraw.Draw(image)
#     font = ImageFont.truetype("arial.ttf", 25)
#     text = "Hello World!"
#     width_text, height_text = font.getsize(text)
#     for i in range(0, width, width_text * 2):
#         for j in range(0, height, height_text * 2):
#             drawer.text((i, j), text, font=font, fill=(0x00, 0xff, 0x00))
#
#     image.show()
#     input("")
#     # image.save(path)


# import sqlite3
# # https://docs.python.org/3.4/library/sqlite3.html
# path = r"C:\Users\ipetrash\Desktop\teller\kmaksimov_NDC.sdb"
# conn = sqlite3.connect(path)
# # result = tuple(row for row in conn .cursor().execute("SELECT * FROM BNA_Demoninations"))
# # for s in result:
# #     print(s)
#
# # cursor = conn .cursor()
# # for row in cursor.execute("SELECT * FROM BNA_Demoninations"):
# #     print(row)
#
# c = conn.cursor()
# result = tuple(row for row in c.execute("SELECT * FROM BNA_Demoninations"))
# print(result)
# print(sorted(result, key=lambda x: x[1]))  # sorting by the second value
#
# # Way to get a list of column names
# print()
# # 1
# print("Column names: {0}".format(c.description))
#
# # 2
# result = tuple(row for row in c.execute("PRAGMA table_info('BNA_Demoninations')"))
# print("Column names: {0}".format(result))
#
# # 3
# conn.row_factory = sqlite3.Row
# c = conn.execute('select * from BNA_Demoninations')
# row = c.fetchone()  # instead of cursor.description
# names = row.keys()
# print("Column names: {0}".format(names))


## Conway's Game of Life (1970).
# Место действия этой игры — «вселенная» — это размеченная на клетки поверхность или плоскость — безграничная,
# ограниченная, или замкнутая (в пределе — бесконечная плоскость).
# Каждая клетка на этой поверхности может находиться в двух состояниях: быть «живой» или быть «мёртвой» (пустой).
# Клетка имеет восемь соседей (окружающих клеток).
# Распределение живых клеток в начале игры называется первым поколением. Каждое следующее поколение рассчитывается
# на основе предыдущего по таким правилам:
# в пустой (мёртвой) клетке, рядом с которой ровно три живые клетки, зарождается жизнь;
# если у живой клетки есть две или три живые соседки, то эта клетка продолжает жить; в противном случае
# (если соседей меньше двух или больше трёх) клетка умирает («от одиночества» или «от перенаселённости»).
# Игра прекращается, если на поле не останется ни одной «живой» клетки, если при очередном шаге ни одна из клеток
# не меняет своего состояния (складывается стабильная конфигурация) или если конфигурация на очередном шаге в
# точности (без сдвигов и поворотов) повторит себя же на одном из более ранних шагов (складывается
# периодическая конфигурация).
#
# Эти простые правила приводят к огромному разнообразию форм, которые могут возникнуть в игре.
#
# Игрок не принимает прямого участия в игре, а лишь расставляет или генерирует начальную конфигурацию «живых»
# клеток, которые затем взаимодействуют согласно правилам уже без его участия (он является наблюдателем).
#
# https://github.com/yangit/Life
# http://habrahabr.ru/post/151832/
# https://ru.wikipedia.org/wiki/%D0%96%D0%B8%D0%B7%D0%BD%D1%8C_%28%D0%B8%D0%B3%D1%80%D0%B0%29#.D0.9F.D1.80.D0.B0.D0.B2.D0.B8.D0.BB.D0.B0
# http://habrahabr.ru/post/140581/
# http://habrahabr.ru/company/mailru/blog/228379/
#
# def print_arr(arr):
#     size = len(arr)
#     for i in range(size):
#         for j in range(size):
#             print(" {} ".format(arr[i][j]), end='')
#         print()
#
# def create_arr(size):
#     arr = []
#     for i in range(size):
#         arr.append([])
#         for j in range(size):
#             arr[i].append(0)
#     return arr
#
# SIZE = 5
# field = create_arr(SIZE)
# print_arr(field)


# TODO: добавить пример работы с модулем json
# https://docs.python.org/3.4/library/json.html
# import json


# TODO: больше примеров по модулю psutil.
# Ссылки:
#   http://pythonhosted.org/psutil/
#   https://github.com/giampaolo/psutil


# # TODO: добавление примеров:
# http://jenyay.net/Matplotlib/Date
# http://jenyay.net/Matplotlib/Text
# http://jenyay.net/Matplotlib/Xkcd
# http://jenyay.net/Matplotlib/Locators
# http://jenyay.net/Matplotlib/LogAxes


# # TODO: datetime
# # dates are easily constructed and formatted
# from datetime import date
# now = date.today()
# # now
# now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B.")
# #'12-02-03. 02 Dec 2003 is a Tuesday on the 02 day of December.'
#
# # dates support calendar arithmetic
# birthday = date(1964, 7, 31)
# age = now - birthday
# print(age.days)


# # Data Compression (модуль zlib)
# >>> import zlib
# >>> s = b'witch which has which witches wrist watch'
# >>> len(s)
# 41
# >>> t = zlib.compress(s)
# >>> len(t)
# 37
# >>> zlib.decompress(t)
# b'witch which has which witches wrist watch'
# >>> zlib.crc32(s)
# 226805979


# # Performance Measurement (модуль timeit)
# >>> from timeit import Timer
# >>> Timer('t=a; a=b; b=t', 'a=1; b=2').timeit()
# 0.57535828626024577
# >>> Timer('a,b = b,a', 'a=1; b=2').timeit()
# 0.54962537085770791
#
#
# ## Quality Control
# # doctest
# def average(values):
#     """Computes the arithmetic mean of a list of numbers.
#
#     >>> print(average([20, 30, 70]))
#     40.0
#     """
#     return sum(values) / len(values)
#
# import doctest
# doctest.testmod()   # automatically validate the embedded tests
#
# # unittest
# import unittest
#
# class TestStatisticalFunctions(unittest.TestCase):
#
#     def test_average(self):
#         self.assertEqual(average([20, 30, 70]), 40.0)
#         self.assertEqual(round(average([1, 5, 7]), 1), 4.3)
#         with self.assertRaises(ZeroDivisionError):
#             average([])
#         with self.assertRaises(TypeError):
#             average(20, 30, 70)
#
# unittest.main() # Calling from the command line invokes all tests
#
#
# # TODO: https://docs.python.org/3/tutorial/stdlib2.html


# TODO: придумать простое приложение и реализовтаь его с помощью TDD (используя unit-тесты)


# # Инвертирование цвета картинки
# from PIL import Image
# import PIL.ImageOps
#
# image_file = r"TowerOfGod_s2_ch100_p02_SIU.png_res.jpg"
# image = Image.open(image_file)
# if image.mode == 'RGBA':
#     r, g, b, a = image.split()
#     rgb_image = Image.merge('RGB', (r, g, b))
#     inverted_image = PIL.ImageOps.invert(rgb_image)
#     r2, g2, b2 = inverted_image.split()
#     final_transparent_image = Image.merge('RGBA', (r2, g2, b2, a))
#     final_transparent_image.save('new_file.png')
# else:
#     inverted_image = PIL.ImageOps.invert(image)
#     inverted_image.save('new_name.png')
#
#
# # TODO: https://gist.github.com/gil9red/021dee2d0be2d15cc04b


# # TODO: получение списка доступных кодировок


# if __name__ == '__main__':
#     from grab import Grab
#
#     def log(mess):
#         from datetime import datetime
#         now = datetime.today().strftime("%d/%m/%y %H:%M")
#         print("{}: {}".format(now, mess))
#
#     g = Grab()
#     g.go("http://www.zikov.ru/")
#
#     last_mess = g.doc.select('//h2[@class="contentheading"]').text()
#     if last_mess != "Седьмая глава":
#         log("Появилось новое сообщение от Зыкова!")
#     else:
#         log("Ничего не поменялось.")
        
        
# TODO: Flask
# "Мега-Учебник Flask, Часть 1: Привет, Мир!": http://habrahabr.ru/post/193242/
# http://ru.wikibooks.org/wiki/Flask


# TODO: Excel
# "Интеграция MS Excel и Python": http://habrahabr.ru/post/232291/


# TODO: tornado
# "Современный Торнадо: распределённый хостинг картинок в 30 строк кода":
# http://habrahabr.ru/post/230607/


# TODO: визуализация связей в вк и linkedin:
# http://habrahabr.ru/post/221251/
# https://github.com/stleon/vk_friends


# TODO: Webmoney API
# http://habrahabr.ru/post/222411/


# TODO: Основы создания 2D персонажа в Godot
# https://github.com/okamstudio/godot/
# "Игровой движок Godot отдали в общественное пользование": http://habrahabr.ru/post/212109/ 
#
# "Часть 1: компилирование игрового движка, создание проекта и анимация покоя героя":
# http://habrahabr.ru/post/212583/
#
# "Часть 2: компилирование шаблонов, немного о GDScript, движение и анимация героя":
# http://habrahabr.ru/post/212837/


# TODO: способы скачивания файлов: http://habrahabr.ru/post/210238/


# TODO: "Экспорт Избранного на Хабре в PDF": http://habrahabr.ru/post/208802/
# Оригинал: https://github.com/vrtx64/fav2pdf
# Форк: https://github.com/icoz/fav2pdf


# TODO: Работа с буфером обмена: pyperclip
# http://stackoverflow.com/questions/11063458/python-script-to-copy-text-to-clipboard


# TODO: скачать ранобе "Непутевый ученик в школе магии" и сконвертировать в формат, который
# сможет открыть книгочиталка.
# Реализовать скрипт в стиле Unix: программа должна делать только одну функцию и делать ее хорошо,
# т.е. один скрипт скачивает главы, и сохраняет их в html на диске, разделяя их на тома (каждый том,
# отдельная папка), а второй скрипт конвертирует эти главы в формат книгочиталки (например, fb2)


# TODO: https://docs.python.org/3/library/collections.html#collections.namedtuple
# >>> # Basic example
# >>> Point = namedtuple('Point', ['x', 'y'])
# >>> p = Point(11, y=22)     # instantiate with positional or keyword arguments
# >>> p[0] + p[1]             # indexable like the plain tuple (11, 22)
# 33
# >>> x, y = p                # unpack like a regular tuple
# >>> x, y
# (11, 22)
# >>> p.x + p.y               # fields also accessible by name
# 33
# >>> p                       # readable __repr__ with a name=value style
# Point(x=11, y=22)


# TODO: brutforce Instagram 
# http://habrahabr.ru/post/215829/
