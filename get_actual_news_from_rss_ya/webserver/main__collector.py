#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'ipetrash'


def get_news_from_rss(url_rss) -> list:
    import feedparser
    rss = feedparser.parse(url_rss)
    return [(entry.title, entry.link) for entry in rss.entries]


def wait(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0):
    from datetime import timedelta, datetime
    today = datetime.today()
    timeout_date = today + timedelta(
        days=days, seconds=seconds, microseconds=microseconds,
        milliseconds=milliseconds, minutes=minutes, hours=hours, weeks=weeks
    )

    while today <= timeout_date:
        def str_timedelta(td):
            # Remove ms
            td = str(td)
            if '.' in td:
                td = td[:td.index('.')]

            return td

        left = timeout_date - today
        left = str_timedelta(left)

        print('\r' * 100, end='')
        print('До следующего запуска осталось {}'.format(left), end='')

        import sys
        sys.stdout.flush()

        # Delay 1 seconds
        import time
        time.sleep(1)

        today = datetime.today()

    print('\r' * 100, end='')
    print('\n')


if __name__ == '__main__':
    from common import *
    init_db()

    while True:
        try:
            news_from_games = get_news_from_rss('https://news.yandex.ru/games.rss')
            print('games', news_from_games)
            append_list_news(news_from_games, interest='games')

            news_from_movies = get_news_from_rss('https://news.yandex.ru/movies.rss')
            print('movies', news_from_movies)
            append_list_news(news_from_movies, interest='movies')

            wait(minutes=4)

        except Exception:
            import traceback
            print('Ошибка:')
            print(traceback.format_exc())

            print('Через 5 минут попробую снова...')

            # Wait 5 minutes before next attempt
            import time
            time.sleep(5 * 60)


    # news_list = get_news_list_and_mark_as_read(interest='games')
    # print(news_list)
    #
    # connect = create_connect()
    # news_list = connect.execute("SELECT * from News").fetchall()
    # print(news_list)


    # from common import create_connect
    #
    # news = get_news('https://news.yandex.ru/games.rss')  # movies
    # print(news)
    #
    # for title, url in news:
    #     # Создание базы и таблицы
    #     connect = create_connect()
    #
    #     interest = 'games'
    #     news_list = connect.execute("SELECT * from News where interest = ?", (interest, )).fetchall()
    #     print(news_list)
    #     quit()
    #
    #     try:
    #         interest = 'games'
    #
    #         connect.execute("INSERT OR IGNORE INTO News (title, url, interest) VALUES (?,?,?)", (title, url, interest))
    #         connect.commit()
    #
    #     finally:
    #         connect.close()


    quit()


    while True:
        try:
            # Перед выполнением, запоминаем дату и время, чтобы иметь потом представление когда
            # в последний раз выполнялось заполнение списка
            from datetime import datetime
            today = datetime.today()
            print(today)


            # Every 5 minutes
            wait(minutes=5)

        except Exception:
            import traceback
            print('Ошибка:')
            print(traceback.format_exc())

            print('Через 5 минут попробую снова...')

            # Wait 5 minutes before next attempt
            import time
            time.sleep(5 * 60)
