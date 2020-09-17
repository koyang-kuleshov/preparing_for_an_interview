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
from random import sample
import os
import re


alphabets = list()
for elem in range(10):
    alphabets.append(
        "".join([itm for itm in sample(string.ascii_lowercase, 10)])
    )
numbers = [itm for itm in sample(range(10, 99), 10)]


def save_file(filename):
    if os.path.exists(filename):
        print(f'{filename} уже существует')
    with open(filename, 'w', encoding='UTF-8') as f_name:
        for row in zip(alphabets, numbers):
            f_name.write(f"{''.join(str(i) for i in row)}\n")


def read_file(filename):
    with open(filename, 'r') as r_file:
        data = r_file.readlines()
    spam = list()
    with open(filename, 'w', encoding='UTF-8') as w_file:
        for row in data:
            line = re.split(r'\d', row)[0] * 2 + '\n'
            print(line)
            spam.append(line)
        w_file.writelines(spam)


save_file('test.txt')
read_file('test.txt')
