"""
Разработать генератор случайных чисел. В функцию передавать начальное и
конечное число генерации (нуль необходимо исключить). Заполнить этими данными
список и словарь. Ключи словаря должны создаваться по шаблону:
“elem_<номер_элемента>”. Вывести содержимое созданных списка и словаря.
"""

import time
import math

random_list = list()
random_dict = dict()


def random_numbers(a, b, count):
    for ind, i in enumerate(range(count), 1):
        spam = (a + b // (b - a)) % time.process_time()
        while spam < a or spam > b or spam == 0:
            spam = spam % time.process_time() * 1000
        random_dict[f'elem_{ind}'] = math.ceil(spam)
        random_list.append(math.floor(spam))
        time.sleep(spam/10)


random_numbers(1, 10, 10)
print(random_list)
print(random_dict)
