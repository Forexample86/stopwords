#!/usr/bin/env python
import subprocess
import os

import docx
from pptx import Presentation
import codecs
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


def pars_docx(paths, file):
    with codecs.open(file, encoding='utf-8') as fin:
        black_list = fin.read().splitlines()
    print(black_list)
    print("Pars .docx")
    for elem in paths:
        if elem.endswith('.docx'):
            doc = docx.Document(elem)
            for paragraph in doc.paragraphs:
                text = paragraph.text.lower()
                for key in black_list:
                    if key in text:
                        print(f"I found {key} word")
                    else:
                        # print("Words not found!")
                        continue


def pars_pptx(paths, file):
    with codecs.open(file, encoding='utf-8') as fin:
        black_list = fin.read().splitlines()
    print(black_list)
    print("Pars .pptx")
    for elem in paths:
        if elem.endswith('.pptx'):
            prs = Presentation(elem)
            for slide in prs.slides:
                for shape in slide.shapes:
                    if hasattr(shape, "text"):
                        shape.text = shape.text.lower()
                        for key in black_list:
                            if key in shape.text:
                                print(f"I found {key} word")
                            else:
                                #print("Words not found!")
                                continue


def pars_md(paths, file):
    with codecs.open(file, encoding='utf-8') as fin:
        black_list = fin.read().splitlines()
    print(black_list)
    print("Pars .md")

    for elem in paths:
        if elem.endswith('.md' or '.markdown'):
            print(elem)
            with codecs.open(elem, encoding='utf-8') as openfile:
                for line in openfile:
                    for key in black_list:
                        if key in line:
                            print(f"I found {key} word")
                        else:
                            #print("Words not found!")
                            continue
