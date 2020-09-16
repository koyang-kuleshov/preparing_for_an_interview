"""
Написать программу, в которой реализовать две функции. В первой должен
создаваться простой текстовый файл. Если файл с таким именем уже существует,
выводим соответствующее сообщение. Необходимо открыть файл и подготовить два
списка: с текстовой и числовой информацией. Для создания списков использовать
генераторы. Применить к спискам функцию zip(). Результат выполнения этой
функции должен должен быть обработан и записан в файл таким образом, чтобы
каждая строка файла содержала текстовое и числовое значение.

Вызвать вторую функцию. В нее должна передаваться ссылка на созданный файл.
Во второй функции необходимо реализовать открытие файла и простой построчный
вывод содержимого. Вся программа должна запускаться по вызову первой функции
"""

import string
import random
import os


alphabets = list()
for elem in range(10):
    alphabets.append(
        "".join([itm for itm in random.sample(string.ascii_lowercase, 10)])
    )
numbers = [itm for itm in random.sample(range(1, 11), 10)]


def save_file(filename):
    if os.path.exists(filename):
        print(f'{filename} уже существует')
    with open(filename, 'w', encoding='UTF-8') as f_name:
        for row in zip(alphabets, numbers):
            f_name.write(f"{''.join(str(i) for i in row)}\n")

    read_file(filename)


def read_file(filename):
    with open(filename, 'r') as r_file:
        for row in r_file:
            print(row)


save_file('test.txt')
