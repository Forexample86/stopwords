"""
Класс для работы с функциями
"""


class Work:
    path = None
    fullname = None
    file_b = None
    file_o = None

    def __init__(self, paths, fullname, file_b, file_o):
        path = paths
        fullname = fullname
        file_b = file_b
        file_o = file_o