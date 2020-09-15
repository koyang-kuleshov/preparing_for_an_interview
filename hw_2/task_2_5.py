"""
Реализовать расчет цены товара со скидкой. Величина скидки должна передаваться
в качестве аргумента в дочерний класс. Выполнить перегрузку методов конструктора
дочернего класса (метод init, в который должна передаваться переменная — скидка)
, и перегрузку метода str дочернего класса. В этом методе должна пересчитываться
цена и возвращаться результат — цена товара со скидкой. Чтобы все работало
корректно, не забудьте инициализировать дочерний и родительский классы
(вторая и третья строка после объявления дочернего класса)
"""


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


class ItemDiscountReport(ItemDiscount):
    def __init__(self, name, price, discount):
        self.discount = discount
        super().__init__(name, price)

    def __str__(self):
        new_price = round((self.get_price * (1 - self.discount / 100)), 2)
        return f'Товар {self.get_name} - цена со скидкой {new_price} руб.'

    def get_parent_data(self):
        return f'{self.get_name()}: {self.get_price()} руб.'


item = ItemDiscountReport('Item #5', 400, 10)
print(item)
