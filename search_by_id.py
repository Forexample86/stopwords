"""
Функция поиска слов по ssh
"""
from scripts import functions as f
from scripts._blacklist import BlackList

OUTPUT = r'data\output.txt'
BLACK_LIST = r'data\black_list.txt'
FILE_CSV = r'data\formats.csv'


def search_by_ssh(ssh):
    black = BlackList()

    black.get_project_by_ssh(ssh)
    fullname = black.get_fullname()

    paths = f.return_paths()

    ret = f.pars_files(paths, fullname, BLACK_LIST, OUTPUT)
    f.csv_out(ret, FILE_CSV)


#
# def pars_docx(paths, fullname, file_b, file_o):
#     print("Pars .docx")
#
#     for elem in paths:
#         if elem.endswith('.docx'):
#             doc = docx.Document(elem)
#             for paragraph in doc.paragraphs:
#                 text = paragraph.text.lower()
#                 for key in black_list(file_b):
#                     if key in text:
#                         print(f"I found {key} word")
#                         output(fullname, key, file_o)
#                     else:
#                         # print("Words not found!")
#                         continue
#                     return key
#
#
# def pars_pptx(paths, fullname, file_b, file_o):
#     print("Pars .pptx")
#
#     for elem in paths:
#         if elem.endswith('.pptx' or '.ppt'):
#             prs = Presentation(elem)
#             for slide in prs.slides:
#                 for shape in slide.shapes:
#                     if hasattr(shape, "text"):
#                         shape.text = shape.text.lower()
#                         for key in black_list(file_b):
#                             if key in shape.text:
#                                 print(f"I found {key} word")
#                                 output(fullname, key, file_o)
#                             else:
#                                 # print("Words not found!")
#                                 continue
#                             return key


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

