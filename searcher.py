"""
Программное средство поиска стоп-слов на gitlab.
"""
import subprocess
import gitlab


def searcher_rep(project_ssh):
    """
    Подключение к gitwork и выгрузка проекта по ssh
    :param project_ssh:
    :return:
    """
    url = 'https://gitwork.ru/'
    token = 'WH-maWZt1ag1bvFsaXKT'
    gl = gitlab.Gitlab(url, private_token=token, api_version='4')
    gl.auth()

    args = ['git', 'clone', project_ssh]
    res = subprocess.Popen(args, stdout=subprocess.PIPE)
    output, _error = res.communicate()
    if not _error:
        print(output)
    else:
        print(_error)


if __name__ == '__main__':
    searcher_rep('git@gitwork.ru:polev/test.git')