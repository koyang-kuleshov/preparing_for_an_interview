"""
Дополнить следующую функцию недостающим кодом:
def print_directory_contents(sPath):

Функция принимает имя каталога и распечатывает его содержимое
в виде «путь и имя файла», а также любые другие
файлы во вложенных каталогах.

Эта функция подобна os.walk. Использовать функцию os.walk
нельзя. Данная задача показывает ваше умение работать с
вложенными структурами.
"""


import os


def print_directory_contents(sPath):
    try:
        spam = os.listdir(sPath)
        if spam:
            print(f'{sPath}: {spam}')
    except Exception:
        pass
    else:
        for root in spam:
            tmp_root = os.path.join(sPath, root)
            cwd_lst = print_directory_contents(tmp_root)
            if cwd_lst:
                print(f'{tmp_root}:{cwd_lst}')


print_directory_contents(os.path.join('..'))
print('*' * 30, 'os.walk', '*' * 30, end='\n')
for root in os.walk(os.path.join('..')):
    print(root)
