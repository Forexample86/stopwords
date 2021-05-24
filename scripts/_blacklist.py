"""
Класс работы с blacklist
"""
import subprocess

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
        self.project = None

    def get_connect(self):
        self.git = gitlab.Gitlab(URL, private_token=TOKEN, api_version='4')
        self.git.auth()
        return self.git

    def set_parse(self, paths, fullname, file_b, file_o):
        self.paths = paths
        self.fullname = fullname
        self.file_b = file_b
        self.file_o = file_o

    def get_project_by_ssh(self, ssh):

        # Получаем проект
        get = get_project(ssh)

        # fullname
        projects = self.git.projects.list()
        for project in projects:
            if project.ssh_url_to_repo == ssh:
                self.project = project
                print(self.project.namespace["name"])
                return self.project.namespace["name"]


def get_project(project_ssh):
    # выкачиваем проект
    args = ['git', 'clone', project_ssh]
    res = subprocess.Popen(args, stdout=subprocess.PIPE)
    out, error = res.communicate()
    if not error:
        print(out)
        return out
    else:
        print(error)
        return error