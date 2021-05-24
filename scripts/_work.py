"""
Класс для работы с функциями
"""


class Work:
    """
    Класс для программы
    """
    path = None
    fullname = None
    file_b = None
    file_o = None

    def __init__(self, paths, fullname, file_b, file_o):
        self.path = paths
        self.fullname = fullname
        self.file_b = file_b
        self.file_o = file_o
