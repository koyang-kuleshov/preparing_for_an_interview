"""
Усовершенствовать первую функцию из предыдущего примера. Необходимо во втором
списке часть строковых значений заменить на значения типа example345
(строка+число). Далее — усовершенствовать вторую функцию из предыдущего примера
(функцию извлечения данных). Дополнительно реализовать поиск определенных
подстрок в файле по следующим условиям: вывод первого вхождения, вывод всех
вхождений. Реализовать замену всех найденных подстрок на новое значение и вывод
всех подстрок, состоящих из букв и цифр и имеющих пробелы только в начале и
конце — например, example345
"""

import string
from random import sample, choice
import os


alphabets = [itm for itm in sample(string.ascii_lowercase, 10)]
numbers = [itm for itm in sample(range(1, 11), 10)]
param = {'search': '3',
         'search_all': 'x',
         'replace_all': 'E',
         }


def save_file(filename):
    if os.path.exists(filename):
        print(f'{filename} уже существует')
    with open(filename, 'w', encoding='UTF-8') as f_name:
        for row in zip(alphabets, numbers):
            if choice((True, False)):
                f_name.write(f'example{row[1]}\n')
            else:
                f_name.write(f"{''.join(str(i) for i in row)}\n")

    read_file(filename, param)


def read_file(filename, param):
    with open(filename, 'r') as r_file:
        search_count = True
        for row in r_file:
            line = f'{row}'
            if (param['search'] and search_count and
                    line.find(param['search']) > -1):
                print(line)
                line.replace(param['search'], param['replace_all'])
                print(line)
                search_count = False
            if param['search_all'] and line.find(param['search_all']) > -1:
                print(line)
                line.replace(param['search'], param['replace_all'])
                print(line)
            if row[0] == ' ' and row[-1] == ' ':
                print(row)


save_file('test.txt')
