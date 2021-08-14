"""
Класс для работы с функциями
"""

# pylint: disable = too-few-public-methods


class Work:
    """
    Класс для объединения данных, необходимых программе
    """
    path = None
    fullname = None
    file_b = None
    file_o = None
    file_csv = None
    scl = ['nomn', 'gent', 'datv', 'accs', 'ablt', 'loct']

    def __init__(self, paths, fullname, file_b, file_o, file_csv):
        self.path = paths
        self.fullname = fullname
        self.file_b = file_b
        self.file_o = file_o
        self.file_csv = file_csv
