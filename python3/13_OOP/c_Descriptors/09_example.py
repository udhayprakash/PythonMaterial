class Account:
    """A simple account class"""

    def __init__(self, owner, amount=0):
        """
        This is the constructor that lets us create
        objects from this class
        """
        self.owner = owner
        self.amount = amount
        self._transactions = []

    def __repr__(self):
        return "Account({!r}, {!r})".format(self.owner, self.amount)

    def __str__(self):
        return "Account of {} with starting amount: {}".format(self.owner, self.amount)

    def add_transaction(self, amount):
        if not isinstance(amount, int):
            raise ValueError("please use int for amount")
        self._transactions.append(amount)

    @property
    def balance(self):
        return self.amount + sum(self._transactions)

    def __len__(self):
        """helps for len() function on instance"""
        return len(self._transactions)

    def __getitem__(self, position):
        """Helps for indexing"""
        return self._transactions[position]


if __name__ == "__main__":
    ram = Account("Ram")
    print(ram)
    print()

    robert = Account("Robert", 10)
    print(robert)
    print(f"{robert =}")
    print()

    print(f"{len(robert) =}")
