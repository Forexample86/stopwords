"""
Класс работы с blacklist
"""
import gitlab
import scripts.methods as s
URL = 'https://gitlab.com/'
TOKEN = 'pKyazBjugLXmwy7Hn1b1'


class BlackList:
    """
    Класс для парсинга проектов
    """
    def __init__(self):
        self.git = None
        self.paths = None
        self.ssh = None
        self.fullname = None
        self.file_b = None
        self.file_o = None
        self.project = None

    def get_connect(self, token):
        """
        Получение объекта соединения с git
        :param token: токен доступа
        :return: объект соединения
        """
        try:
            self.git = gitlab.Gitlab(URL, private_token=token, api_version='4')
            self.git.auth()
        except gitlab.GitlabAuthenticationError as err:
            raise ConnectionError('Ошибка входа в git!') from err

        return self.git

    def get_project_by_ssh(self, ssh):
        """
        Получение project
        Args:
            ssh: доступ

        """
        s.get_project(ssh)
        self.ssh = ssh

    def get_fullname(self, name):
        """
        Получение имя пользователя проекта
        :return: fullname
        """
        # fullname
        project = self.git.projects.list(search=name)
        self.project = project
        self.fullname = self.project.name
        return self.fullname
