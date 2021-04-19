"""
Программное средство поиска стоп-слов на gitlab.
"""
import subprocess
import gitlab
import os
import codecs
import docx


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


def searcher_files(file):
    """
    Чтение из файла списка нехороших слов и парсинг docx файлов на анличие нехороших слов
    :param file:
    :return:
    """
    with codecs.open(file, encoding='utf-8') as fin:
        black_list = fin.read().splitlines()
    print(black_list)

    paths = []
    folder = os.getcwd()
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith('.docx') and not file.startswith('~'):
                paths.append(os.path.join(root, file))

    for path in paths:
        doc = docx.Document(path)
        for paragraph in doc.paragraphs:
            text = paragraph.text.lower()
            for key in black_list:
                if key in text:
                    print(f"I found {key} words")
                else:
                    continue


if __name__ == '__main__':
    searcher_rep('git@gitwork.ru:polev/test.git')
    searcher_files(r'C:\Users\polev\PycharmProjects\prac\2018-3-23-pol\black_list.txt')
