import subprocess
import os
import logging
import warnings as w

import docx
from pptx import Presentation
import codecs
import gitlab
from gitlab import *

URL = 'https://gitwork.ru/'
TOKEN = 'WH-maWZt1ag1bvFsaXKT'


def searcher_rep(project_ssh):
    """
    Подключение к gitwork и выгрузка проекта по ssh
    :param project_ssh:
    :return:
    """
    # git@gitwork.ru:polev/test.git
    # https://gitwork.ru/polev/test.git
    gl = None
    try:
        gl = gitlab.Gitlab(URL, private_token=TOKEN, api_version='4')
        gl.auth()
    except gitlab.GitlabAuthenticationError as err:
        print(err.error_message)
        w.warn(err.error_message, Warning)
        return err.error_message

    # выкачиваем проект
    args = ['git', 'clone', project_ssh]
    res = subprocess.Popen(args, stdout=subprocess.PIPE)
    output, error = res.communicate()
    if not error:
        print(output)
    else:
        print(error)

    # fullname
    try:
        projects = gl.projects.list()
        for project in projects:
            if project.ssh_url_to_repo == project_ssh:
                project_ = project
                print(project_.namespace["name"])
                return project_.namespace["name"]
    except gitlab.GitlabListError as err:
        w.warn(err.error_message, Warning)


def searcher_files():
    """
    :return: paths
    """
    suffix = ('.docx', '.doc', '.pptx', '.md')
    paths = []
    folder = os.getcwd()
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith(suffix) and not file.startswith('~'):
                paths.append(os.path.join(root, file))
    #  Конвертер doc в docx(работает в linux через libre office)
    #  args = ['soffice', '--headless', '--convert-to', 'docx', ]
    #  for count in paths:
    #      if count.endswith('.doc'):
    #          print(count)
    #          subprocess.Popen([args, count], stdout=subprocess.PIPE)
    return paths


def black_list(file):
    with codecs.open(file, 'r', encoding='utf-8') as fin:
        black = fin.read().splitlines()
    return black


def output(fullname, word, file):
    text = f"fullname:  {fullname}  ' | '  stop word: {word}"
    with codecs.open(file, "a", encoding='utf-8') as fin:
        out = fin.write(text + '\n')
        fin.close()
    return out


def pars_docx(paths, fullname, file_b, file_o):
    print("Pars .docx")

    for elem in paths:
        if elem.endswith('.docx'):
            doc = docx.Document(elem)
            for paragraph in doc.paragraphs:
                text = paragraph.text.lower()
                for key in black_list(file_b):
                    if key in text:
                        print(f"I found {key} word")
                        output(fullname, key, file_o)
                    else:
                        # print("Words not found!")
                        continue
                    return key


def pars_pptx(paths, fullname, file_b, file_o):
    print("Pars .pptx")

    for elem in paths:
        if elem.endswith('.pptx'):
            prs = Presentation(elem)
            for slide in prs.slides:
                for shape in slide.shapes:
                    if hasattr(shape, "text"):
                        shape.text = shape.text.lower()
                        for key in black_list(file_b):
                            if key in shape.text:
                                print(f"I found {key} word")
                                output(fullname, key, file_o)
                            else:
                                # print("Words not found!")
                                continue
                            return key


def pars_md(paths, fullname, file_b, file_o):
    print("Pars .md")

    for elem in paths:
        if elem.endswith('.md' or '.markdown'):
            with codecs.open(elem, encoding='utf-8') as openfile:
                for line in openfile:
                    for key in black_list(file_b):
                        if key in line:
                            print(f"I found {key} word")
                            output(fullname, key, file_o)
                        else:
                            # print("Words not found!")
                            continue
                        return key


with w.catch_warnings(record=True) as warnings:
    w.simplefilter("always")

for out in warnings:
    print(str(out.message))
