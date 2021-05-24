"""
Поиск по всем репозиториям
"""
from scripts._blacklist import BlackList
from scripts.functions import pars_files


def search_all():
    git = BlackList()
    git = git.get_connect()
    for n in git.projects.list():
        pars_files()

