import argparse
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
    parser.add_argument('-f', '--file_formats', type=str, default=None, help='Enter path to csv file for output formats')
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
