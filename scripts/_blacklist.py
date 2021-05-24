"""
Класс работы с blacklist
"""
import gitlab

URL = 'https://gitwork.ru/'
TOKEN = 'WH-maWZt1ag1bvFsaXKT'


class BlackList:
    def __init__(self):
        self.git = None
        self.paths = None
        self.fullname = None
        self.file_b = None
        self.file_o = None

    def get_connect(self):
        self.git = gitlab.Gitlab(URL, private_token=TOKEN, api_version='4')
        self.git.auth()
        return self.git

    def set_parse(self, paths, fullname, file_b, file_o):
        self.paths = paths
        self.fullname = fullname
        self.file_b = file_b
        self.file_o = file_o
