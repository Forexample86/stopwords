# Назначение программного средства

Программное средство позволяет:

- Искать стоп-слова из black_list в файлах всех проектов в gitlab.
- Искать стоп-слова из black_list в файлах проекта по его ssh.
- Выводить статистику по файлам с заданными расширениями в csv файл.

# Важное примечание
    
    Для того, чтобы все работало, необходимо поместить файлы id.rsa, id_rsa.pub из своего файла .ssh в корень проекта.

# Запуск pylint

    pylint main.py - pylint для main
---
    pylint methods.py - pylint для методов
# Запуск тестов

    python /test/test.py <аргументы> --token <токен>

# Опциональные аргументы:
Show this help message and exit

    -h, --help

Input key for work

    -t TOKEN, --token TOKEN

View all projects for stop-words

    -a, --all

Input ssh project for search stop-words

    -s SSH, --project_ssh SSH

Input file with stop-words

    -b PATH, --black_list PATH

Input file for output information

    -o PATH, --output PATH

Input file for file statistics

    -f PATH, --file_formats PATH


# Docker
**Построение docker образа**

```bash
	sudo docker build -t stopwords .
```

**Запуск docker контейнера**

```bash
	docker run --rm -p 8080:8080 -it stopwords -a -t <token> -b /code/data/black_list.txt -f /code/data/formats.csv -o /code/data/output.txt 
```

**Возможные опции:**

-s(--project_ssh) <ssh> - поиск слов в проекте по его ssh:

```bash
	docker run --rm -p 8080:8080 -it stopwords -s <ssh> -t <token> -b /code/data/black_list.txt -f /code/data/formats.csv -o /code/data/output.txt 
```

-a(--all) - поиск слов во всех проектах:

```bash
	docker run --rm -p 8080:8080 -it stopwords -a -t <token> -b /code/data/black_list.txt -f /code/data/formats.csv -o /code/data/output.txt 
```
