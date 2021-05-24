"""
Функции для работы
"""

import docx
from pptx import Presentation
from scripts._blacklist import BlackList
from scripts._work import Work
import codecs


def black_list(file):
    with codecs.open(file, 'r', encoding='utf-8') as fin:
        black = fin.read().splitlines()
    return black


def output(work, key):
    text = f"fullname:  {work.fullname}  ' | '  stop word: {key}"
    with codecs.open(work.file_o, "a", encoding='utf-8') as fin:
        out = fin.write(text + '\n')
        fin.close()
    return out


def pars_files(paths, fullname, file_b, file_o):
    """
    Функция парсинга файлов
    Args:
        paths: пути
        fullname:
        file_b:
        file_o:

    Returns:

    """
    print("Pars .md")
    work = Work(paths, fullname, file_b, file_o)
    for elem in paths:
        if elem.endswith('.md' or '.txt'):
            check_word(elem, work)

        if elem.endswith('.pptx' or '.ppt'):
            check_pptx(elem, work)

        if elem.endswith('.docx'):
            check_docx(elem, work)


def check_word(elem, work):
    """
    Проверка word
    Args:
        elem: изучаемый объект
        work: класс с переменными

    Returns:

    """
    with codecs.open(elem, encoding='utf-8') as openfile:
        for line in openfile:
            for key in black_list(work.file_b):
                if key in line:
                    print(f"I found {key} word")
                    output(work, key)
                else:
                    # print("Words not found!")
                    continue
                return key


def check_pptx(elem, work):
    """
    Проверка pptx
    Args:
        elem: изучаемый объект
        work: класс с переменными

    Returns:

    """
    prs = Presentation(elem)
    for slide in prs.slides:
        for shape in slide.shapes:
            if hasattr(shape, "text"):
                shape.text = shape.text.lower()
                for key in black_list(work.file_b):
                    if key in shape.text:
                        print(f"I found {key} word")
                        output(work, key)
                    else:
                        # print("Words not found!")
                        continue
                    return key


def check_docx(elem, work):
    """
    Проверка docx
    Args:
        elem: изучаемый объект
        work: класс с переменными

    Returns:

    """
    doc = docx.Document(elem)
    for paragraph in doc.paragraphs:
        text = paragraph.text.lower()
        for key in black_list(work.file_b):
            if key in text:
                print(f"I found {key} word")
                output(work, key)
            else:
                # print("Words not found!")
                continue
            return key
