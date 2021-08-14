"""
Поиск по ssh
"""
from scripts import methods as f
from scripts._blacklist import BlackList


def search_by_ssh(ssh, token, output, blacklist, file_csv):
    """
    :param token: токен доступа
    :param ssh: ключ для проекта
    :param file_csv: файл для статистики
    :param blacklist: файл с плохими словами
    :param output: файл для вывода логов
    """
    black = BlackList()
    black.get_connect(token)
    # Получаем проект
    black.get_project_by_ssh(ssh)
    project_name = f.get_proj_name(ssh)
    fullname = black.get_fullname(project_name)
    # Получаем пути и парсим файлы
    paths = f.return_paths()
    print('Ищу в файлах.. ')
    ret = f.pars_files(paths, fullname, blacklist, output)

    # Выводим в файл
    if ret:
        f.csv_out(ret, file_csv)

    f.delete_project(project_name.lower())
    print('Проект ' + fullname + ' удален. ')
