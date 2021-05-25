#!/usr/bin/env python3
"""
Программное средство поиска стоп-слов на gitlab.
"""

from search_by_id import search_by_ssh
OUTPUT = r'data\output.txt'
BLACK_LIST = r'data\black_list.txt'
FILE_CSV = r'data\formats.csv'


if __name__ == '__main__':
    #fullname = search_by_id.searcher_rep('git@gitwork.ru:polev/test.git')
    #paths = search_by_id.searcher_files()
    ssh = input()
    try:
        search_by_ssh(ssh)
    except Exception as e:
        print()
    search_by_id.csv_out(search_by_id.search_expansion(), FILE_CSV)

