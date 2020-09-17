"""
Реализовать возможность переустановки значения цены товара. Необходимо, чтобы и
родительский, и дочерний классы получили новое значение цены. Следует проверить
это, вызвав соответствующий метод родительского класса и функцию дочернего
(функция, отвечающая за отображение информации о товаре в одной строке)
"""


class ItemDiscount:

    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    def set_price(self, price):
        self.__price = price

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    @property
    def get_parent_class_data(self):
        return f'Данные в родительском классе: {self.__name}: {self.__price}'


class ItemDiscountReport(ItemDiscount):
    def get_parent_data(self):
        return f'{self.get_name()}: {self.get_price()} руб.'


item = ItemDiscountReport('Item #4', 400)
print(item.get_parent_data())
item.set_price(300)
print(item.get_parent_data())
