"""
Написать программу, которая будет содержать функцию для получения имени файла
из полного пути до него. При вызове функции в качестве аргумента должно
передаваться имя файла с расширением. В функции необходимо реализовать поиск
полного пути по имени файла, а затем «выделение» из этого пути имени файла
(без расширения)
"""

import os


def get_filename(source):
    fullpath = os.path.abspath(source)
    base = os.path.basename(fullpath)
    return base.split('.')[0]


print(get_filename('task_3_1.py'))
