"""
Написать функцию, реализующую вывод таблицы умножения размерностью AｘB.
Первый и второй множитель должны задаваться в виде аргументов функции.
Значения каждой строки таблицы должны быть представлены списком, который
формируется в цикле. После этого осуществляется вызов внешней lambda-функции,
которая формирует на основе списка строку. Полученная строка выводится в
главной функции. Элементы строки (элементы таблицы умножения) должны
разделяться табуляцией.
"""


def get_table_results(a, b):
    for row in range(a + 1):
        row_lst = list()
        for col in range(b + 1):
            if row == 0:
                row_lst.append(col)
            elif col == 0:
                row_lst.append(row)
            else:
                row_lst.append(row * col)
        print("\t".join([str(i) for i in row_lst]))


get_table_results(5, 5)