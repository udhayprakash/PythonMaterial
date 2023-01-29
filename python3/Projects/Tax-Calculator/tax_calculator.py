#!/usr/bin/python3
"""
Purpose:
    Federal Tax Rates for 2020
        15%     on the first $48,535 of taxable income, plus
        20.5%   on the next $48,534 of taxable income (on the portion of taxable income over 48,535 up to $97,069), plus
        26%     on the next $53,404 of taxable income (on the portion of taxable income over $97,069 up to $150,473), plus
        29%     on the next $63,895 of taxable income (on the portion of taxable income over 150,473 up to $214,368), plus
        33%     of taxable income over $214,368
"""


class TaxCalculator(object):
    """
    Tax calculator class
    """

    def __init__(self):
        """Constructor"""
        self.salary = 0
        self.tax_amount = 0

    def calculate_tax(self, salary):
        """
        This public function is responsible for converting salary to float
        and call protected method self._calculate_tax()
        :param salary:
        :return: Tax Amount (float)
        """
        self.tax_amount = 0
        try:
            # input cleansing
            salary = str(salary).strip(" $").replace(",", "")
            salary = salary.upper().split("CAD")[-1]
            self.salary = float(salary)
        except ValueError:
            print("Invalid input")
            return "Invalid input"
        return self._calculate_tax()

    def _calculate_tax(self):
        """
        This function calculates the TAX amount for the given salary
        :return: tax amount (float)
        """
        remaining_amount = self.salary
        if remaining_amount > 214368:
            slab_amount = remaining_amount - 214368
            self.tax_amount += slab_amount * 33 / 100
            remaining_amount = 214368

        if 150473 < remaining_amount <= 214368:
            slab_amount = remaining_amount - 150473
            self.tax_amount += slab_amount * 29 / 100
            remaining_amount = 150473

        if 97069 < remaining_amount <= 150473:
            slab_amount = remaining_amount - 97069
            self.tax_amount += slab_amount * 26 / 100
            remaining_amount = 97069

        if 48535 < remaining_amount <= 97069:
            slab_amount = remaining_amount - 48535
            self.tax_amount += slab_amount * 20.5 / 100
            remaining_amount = 48535

        if 0 < remaining_amount <= 97069:
            slab_amount = remaining_amount
            self.tax_amount += slab_amount * 15 / 100

        self.tax_amount = round(self.tax_amount, 2)
        print(
            f"""
            Salary          : {round(self.salary, 2):10}
            Tax Amount      : {self.tax_amount:10}
            """
        )

        return self.tax_amount


if __name__ == "__main__":
    # Step 1: Instantiation
    tc = TaxCalculator()

    # Step 2: Get salary amount in run-time
    sal = input("Enter your salary( in CAD):")

    # Step 3: Calculate the Tax Amount
    tc.calculate_tax(sal)
