import unittest

from scripts import methods


class TestMethods(unittest.TestCase):

    def clear_file(self):
        self.assertTrue(methods.clear_file(r'..\data\output.txt'))

    def get_proj_name(self):
        ssh = 'git@gitlab.com:test_id-/test_project.git'
        self.assertEqual(methods.get_proj_name(ssh), 'test_project')

    def get_wrong_proj(self):
        with self.assertRaises(OSError) as context:
            methods.get_project('wrong_ssh')
        self.assertTrue('Ошибка загрузки' in str(context.exception))

    def delete_wrong_project(self):
        with self.assertRaises(FileNotFoundError) as context:
            methods.delete_project('wrong_name')
        self.assertTrue('Системе не удается найти указанный путь '
                        './wrong_name' in str(context.exception))

    def test_parse_first(self):
        text = 'Лейтенантов нашли за забором'
        blacklist = ['лейтенант']
        self.assertEqual('лейтенант', methods.parse(text, blacklist))

    def test_parse_second(self):
        text = 'Почему нет техника на месте? '
        blacklist = ['техник']
        self.assertEqual('техник', methods.parse(text, blacklist))

    def black_list(self):
        self.assertEqual(methods.black_list(r'.\blacklist'), ['эвм', 'докер'])


if __name__ == '__main__':
    unittest.main()
