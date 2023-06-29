"""
Purpose: Module coupling, or tight coupling
    It refers to the degree of interdependence between modules in a software system.
    It occurs when modules are closely connected and rely heavily on each other's internal details and implementation.
    Tight coupling can make the system less flexible, maintainable, and reusable.

    ----------------------------------------------------
    Feature	        | Composition	    | Tight Coupling
    ----------------------------------------------------
    Dependencies	| Loose	            | Tight
    Flexibility	    | More flexible	    | Less flexible
    Reusability	    | More reusable	    | Less reusable
    ----------------------------------------------------

"""


class Stock:
    def __init__(self, symbol, price):
        self.symbol = symbol
        self.price = price

    def get_symbol(self):
        return self.symbol

    def get_price(self):
        return self.price


class Portfolio:
    def __init__(self, stocks):
        self.stocks = stocks

    def get_total_value(self):
        total_value = 0
        for stock in self.stocks:
            total_value += stock.get_price()
        return total_value


class TightCouplingPortfolio(Portfolio):
    def __init__(self, stocks):
        super().__init__(stocks)
        self.apple_stock = stocks[0]
        self.google_stock = stocks[1]

    def get_apple_stock_value(self):
        return self.apple_stock.get_price()

    def get_google_stock_value(self):
        return self.google_stock.get_price()
