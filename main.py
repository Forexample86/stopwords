#!/usr/bin/env python3
"""
Программное средство поиска стоп-слов на gitlab.
"""
import sys

from search_by_id import search_by_ssh
from search_all import search_all
from scripts.args import parse_args, check_args
from scripts.methods import clear_file_logger, clear_file_csv

# Дефолтные места
OUTPUT = r'.\data\output.txt'
BLACK_LIST = r'.\data\black_list.txt'
FILE_CSV = r'.\data\formats.csv'


if __name__ == '__main__':

    ARGS = parse_args()
    TOKEN = ARGS.token
    ALL = ARGS.all
    SSH = ARGS.project_ssh
    BLACK_LIST = ARGS.black_list
    FILE_OUTPUT = ARGS.output
    FILE_CSV = ARGS.file_formats
    try:
        check_args(ARGS)
        clear_file_logger(FILE_OUTPUT)
        clear_file_csv(FILE_CSV)
        if ALL:
            search_all(TOKEN, FILE_OUTPUT, BLACK_LIST, FILE_CSV)
        search_by_ssh(SSH, TOKEN, FILE_OUTPUT, BLACK_LIST, FILE_CSV)
    except ValueError as v:
        sys.exit(v)
    except FileNotFoundError as f:
        sys.exit(f)
    except ConnectionError as c:
        sys.exit(c)
    except OSError as o:
        sys.exit(o)
