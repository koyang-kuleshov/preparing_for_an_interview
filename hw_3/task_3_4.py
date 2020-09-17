"""
Создать два списка с различным количеством элементов. В первом должны быть
записаны ключи, во втором — значения. Необходимо написать функцию, создающую из
данных ключей и значений словарь. Если ключу не хватает значения, в словаре для
него должно сохраняться значение None. Значения, которым не хватило ключей,
необходимо отбросить
"""


import string
from random import randint, sample


alphabets = [itm for itm in sample(string.ascii_lowercase, randint(1, 10))]
numbers = [itm for itm in sample(range(1, 11), randint(1, 10))]


def make_dict(keys, values):
    spam = dict()
    for value, key in enumerate(keys):
        try:
            values[value]
        except IndexError:
            spam[key] = None
        else:
            spam[key] = value
    return spam


print(make_dict(alphabets, numbers))
