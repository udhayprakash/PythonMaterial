class Pricer:
    DISCOUNT = 0.80

    def get_discounted_price(self, price):
        return price * self.DISCOUNT


if __name__ == "__main__":
    pricer = Pricer()
    pricer.DISCOUNT = 0.5
    assert pricer.get_discounted_price(100) == 50.0

    Pricer.DISCOUNT = 0.75
    pricer = Pricer()
    assert pricer.get_discounted_price(100), 75.0
