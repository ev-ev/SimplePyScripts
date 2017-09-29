#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'ipetrash'


from config import LOGIN, PASSWORD


def create_connect():
    import sqlite3
    return sqlite3.connect('gist_commits.sqlite')


def init_db():
    # Создание базы и таблицы
    with create_connect() as connect:
        connect.execute('''
            CREATE TABLE IF NOT EXISTS GistFile (
                id INTEGER PRIMARY KEY,
                commit_hash TEXT NOT NULL,
                committed_at DATETIME NOT NULL,
                raw_url TEXT NOT NULL,
                content CLOB NOT NULL,
                
                CONSTRAINT raw_url_unique UNIQUE (commit_hash, raw_url)
            );
        ''')

        connect.commit()


if __name__ == '__main__':
    init_db()

    from github import Github
    gh = Github(LOGIN, PASSWORD)
    # #
    # # OR:
    # # But: "github.GithubException.RateLimitExceededException: 403 {'message': "API rate limit exceeded for \
    # # 79.000.10.000. (But here's the good news: Authenticated requests get a higher rate limit. Check out the
    # # documentation for more details.)", 'documentation_url': 'https://developer.github.com/v3/#rate-limiting'}"
    # gh = Github()

    gist = gh.get_gist('2f80a34fb601cd685353')
    print(gist)
    print('History ({}):'.format(len(gist.history)))

    with create_connect() as connect:
        for history in reversed(gist.history):
            print('  committed_at: {}, version: {}, files: {}'.format(
                history.committed_at, history.version, history.files)
            )

            file = history.files['gistfile1.txt']
            # print('    url: {}'.format(file.raw_url))
            # print('    [{}]: {}'.format(len(file.content), repr(file.content)[:150]))
            # print()

            connect.execute(
                'INSERT OR IGNORE INTO GistFile (commit_hash, committed_at, raw_url, content) VALUES (?, ?, ?, ?)',
                (history.version, history.committed_at, file.raw_url, file.content)
            )

        connect.commit()