#!/usr/bin/env python3

"""
Программное средство поиска стоп-слов на gitlab.
"""
import argparse
import search_by_id

"""
Обработка аргументов в cli

Methods:
    parse_args - добавление парсера
    check_args - проверка аргументов на корректность
"""


def parse_args():
    """
    Args:
        parser: парсер
    Returns: аргументы для парсера
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--token', type=str, default='Key', help='Enter key for work')
    parser.add_argument('-s', '--project-ssh', type=str, default='SSH', help='Enter ssh project for clone')
    parser.add_argument('-b', '--black-list', type=str, default=None, help='Enter path to file with black list')
    parser.add_argument('-o', '--output', type=str, default=None, help='Enter path to file for output')
    return parser.parse_args()


def check_args(args):
    """
    Функция проверки подаваемых аргументов
    Args:
        args: Словарь подаваемых аргументов

    Returns:
        True - если все верно

    Raises:
        FileNotFoundError - файл не может быть найден
        ValueError - неверное название группы/подгруппы
    """
    if not args.get('token'):
        raise ValueError("Token not entered")


if __name__ == '__main__':
    output = r'data\output.txt'
    black_list = r'data\black_list.txt'
    file_csv = r'data\formats.csv'
    #fullname = search_by_id.searcher_rep('git@gitwork.ru:polev/test.git')
    #paths = search_by_id.searcher_files()
    data = search_by_id.search_expansion()
    search_by_id.csv_out(data, file_csv)
    #search_by_id.pars_docx(paths, fullname, black_list, output)
    #search_by_id.pars_pptx(paths, fullname, black_list, output)
    #search_by_id.pars_md(paths, fullname, black_list, output)

    #stop_word = search_by_id.black_list(file=black_list)
    #search_by_id.output(fullname, stop_word, file=output)

