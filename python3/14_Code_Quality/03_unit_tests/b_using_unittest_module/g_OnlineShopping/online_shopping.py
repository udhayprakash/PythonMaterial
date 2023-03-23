#!/usr/bin/python
"""
Purpose:
"""


class Item:
    def __init__(self, item, price):
        if not isinstance(item, str):
            raise ValueError("Invalid Item name data type")

        self.item = item
        self.price = float(price)

    def __repr__(self) -> str:
        return "{} price is {}".format(self.item, self.price)

    __str__ = __repr__


class ShoppingCart(object):
    def __init__(self):
        self.items = []

    def add(self, item, price):
        self.items.append(Item(item, price))
        return self

    def item(self, index):
        return self.items[index - 1].item

    def price(self, index):
        return self.items[index - 1].price

    def total(self, sales_tax):
        sum_price = sum([item.price for item in self.items])
        return sum_price * (1.0 + sales_tax / 100.0)

    def __len__(self):
        return len(self.items)
