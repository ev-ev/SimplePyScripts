#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'ipetrash'


from urllib.parse import urljoin
from urllib.request import urlopen

from bs4 import BeautifulSoup


if __name__ == '__main__':
    url = 'http://www.jazzcinema.ru/'

    with urlopen(url) as f:
        root = BeautifulSoup(f.read(), 'lxml')

        # Список расписаний, первый в списке -- текущий день
        schedule_list = root.select('.schedule')

        schedule = schedule_list[0]

        from datetime import datetime
        schedule_date = datetime.strptime(schedule['rel'], 'calendar-%Y-%m-%d-schedule').strftime('%d/%m/%Y')
        print('Расписание фильмов за {}:'.format(schedule_date))

        # Получение фильмов в текущей вкладке (по идеи, текущая вкладка -- текущий день)
        for border in schedule.select('.border'):
            a = border.select_one('.movie .title > a')
            url = urljoin(url, a['href'])
            print(a['title'], url)
            print('   ', border.select_one('.genre').text)

            for seanse in border.select('.seanses'):
                time = seanse.select_one('a').text
                price = seanse.select_one('.price').text
                print('    {} : {}'.format(time, price))

            print()