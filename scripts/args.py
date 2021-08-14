"""
Создание аргументов для программы
"""
import argparse
import codecs

OUTPUT = r'data\output.txt'
BLACK_LIST = r'data\black_list.txt'
FILE_CSV = r'data\formats.csv'

"""
Обработка аргументов в cli

Methods:
    parse_args - добавление парсера
    check_args - проверка аргументов на корректность
"""

# pylint: disable = line-too-long

def parse_args():
    """
    Args:
    Returns: аргументы для парсера
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--token', type=str, default='Key', help='Enter key for work')
    parser.add_argument('-a', '--all', action='store_true', default=False, help='Scan for all projects')
    parser.add_argument('-s', '--project_ssh', type=str, default=None, help='Enter ssh project for clone')
    parser.add_argument('-b', '--black_list', type=str, default=r'data\black_list.txt', help='Enter path to file with black list')
    parser.add_argument('-o', '--output', type=str, default=r'data\output.txt', help='Enter path to file for output')
    parser.add_argument('-f', '--file_formats', type=str, default=r'data\formats.csv', help='Enter path to csv file for output formats')
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
        raise ValueError('Вы не ввели токен! ')

    try:
        with codecs.open(args.get('token'), 'r', encoding='utf-8') as fin:
            fin.close()
    except FileNotFoundError as err:
        raise FileNotFoundError('Не могу открыть файл blacklist') from err
