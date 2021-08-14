"""
Поиск по всем репозиториям
"""

from scripts import methods as f
from scripts._blacklist import BlackList


# Добавить выкачку любого проекта
def search_all(token, output, blacklist, file_csv):
    """
    :param token: токен доступа
    :param file_csv: файл для статистики
    :param blacklist: файл с плохими словами
    :param output: файл для вывода логов
    Поиск по всем репозиториям
    """
    black = BlackList()
    git = black.get_connect(token)
    for project in git.projects.list():
        ssh = project.ssh_url_to_repo

        # Получаем проект, получаем нужные переменные
        black.get_project_by_ssh(ssh)
        project_name = project.name
        fullname = black.get_fullname(project_name)
        paths = f.return_paths()
        print('Ищу в файлах.. ')
        # Парсим, выводим нужное
        ret = f.pars_files(paths, fullname, blacklist, output)
        f.csv_out(ret, file_csv)

        # Удаляем проект
        f.delete_project(project_name.lower())
        print('Проект ' + fullname + ' удален. ')
