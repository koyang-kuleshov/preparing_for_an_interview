"""
Проверить на практике возможности полиморфизма. Необходимо разделить дочерний
класс ItemDiscountReport на два класса. Инициализировать классы необязательно.
Внутри каждого поместить функцию get_info, которая в первом классе будет
отвечать за вывод названия товара, а вторая — его цены. Далее реализовать
выполнение каждой из функции тремя способами
"""


def object_handler(obj):
    print(obj.get_info)


class ItemDiscount:

    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    def set_price(self, price):
        self.__price = price

    @property
    def get_name(self):
        return self.__name

    @property
    def get_price(self):
        return self.__price

    @property
    def get_parent_class_data(self):
        return f'Данные в родительском классе: {self.__name}: {self.__price}'


class ItemDiscountReportOne(ItemDiscount):
    def __init__(self, name, price, discount):
        self.discount = discount
        super().__init__(name, price)

    def __str__(self):
        new_price = round((self.get_price * (1 - self.discount / 100)), 2)
        return f'Товар {self.get_name} - цена со скидкой {new_price} руб.'

    def get_parent_data(self):
        return f'{self.get_name()}: {self.get_price()} руб.'

    @property
    def get_info(self):
        return f'Название товара: {self.get_name}'


class ItemDiscountReportTwo(ItemDiscount):
    def __init__(self, name, price, discount):
        self.discount = discount
        super().__init__(name, price)

    def __str__(self):
        new_price = round((self.get_price * (1 - self.discount / 100)), 2)
        return f'Товар {self.get_name} - цена со скидкой {new_price} руб.'

    def get_parent_data(self):
        return f'{self.get_name()}: {self.get_price()} руб.'

    @property
    def get_info(self):
        return f'Цена товара: {self.get_price}'


item_one = ItemDiscountReportOne('Item #61', 400, 10)
item_two = ItemDiscountReportTwo('Item #62', 420, 5)
print(item_one.get_info)
print(item_two.get_info)

for obj in (item_two, item_one):
    print(obj.get_info)

for obj in (item_one, item_two):
    object_handler(obj)
