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
    ret = f.pars_files(paths, fullname, blacklist, output)

    # Выводим в файл
    if ret:
        f.csv_out(ret, file_csv)

    #f.delete_project(project_name.lower())

#
# def searcher_rep(project_ssh):
#     """
#     Подключение к gitwork и выгрузка проекта по ssh
#     :param project_ssh:
#     :return:
#     """
#     # git@gitwork.ru:polev/test.git
#     # https://gitwork.ru/polev/test.git
#
#     try:
#         gl = BlackList()
#         gl = gl.get_connect()
#     except gitlab.GitlabAuthenticationError as err:
#         w.warn(err.error_message, Warning)
#         return err.error_message
#
#     # Получаем проект
#     get = get_project(project_ssh)
#
#     # fullname
#     try:
#         projects = gl.projects.list()
#         for project in projects:
#             if project.ssh_url_to_repo == project_ssh:
#                 project_ = project
#                 print(project_.namespace["name"])
#                 return project_.namespace["name"]
#     except gitlab.GitlabListError as err:
#         w.warn(err.error_message, Warning)
