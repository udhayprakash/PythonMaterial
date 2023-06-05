import unittest

from online_shopping import Item, ShoppingCart


class TestItem(unittest.TestCase):
    def test_positive_item_creation(self):
        item_created = Item("bag", 34)
        self.assertEqual(item_created.item, "bag")
        self.assertEqual(item_created.price, 34)

    def test_negative_item_creation(self):
        item_created = Item("bag", 34)
        self.assertNotEqual(item_created.item, "pen")
        self.assertNotEqual(item_created.price, 35)

    def test_positive_all_data_type_inputs(self):
        item_created = Item("bag", 34)
        self.assertIsInstance(item_created.item, str)
        self.assertIsInstance(item_created.price, float)

    def test_negative_all_data_type_inputs(self):
        # with self.assertRaises(ValueError) as err:
        #     Item("pen", 34)
        # AssertionError: ValueError not raised

        with self.assertRaises(Exception) as err:
            Item(23123123, 34)

        self.assertEqual("Invalid Item name data type", str(err.exception))

        with self.assertRaises(ValueError) as err:
            Item(True, 34)

        self.assertEqual("Invalid Item name data type", str(err.exception))


class TestShoppingCart(unittest.TestCase):
    def test_add_item(self):
        cart = ShoppingCart()
        cart.add("Item 1", 10)
        cart.add("Item 2", 20)
        self.assertEqual(len(cart), 2)

    def test_item_name(self):
        cart = ShoppingCart()
        cart.add("Item 1", 10)
        cart.add("Item 2", 20)
        self.assertEqual(cart.item(1), "Item 1")
        self.assertEqual(cart.item(2), "Item 2")

    def test_item_price(self):
        cart = ShoppingCart()
        cart.add("Item 1", 10)
        cart.add("Item 2", 20)
        self.assertEqual(cart.price(1), 10)
        self.assertEqual(cart.price(2), 20)

    def test_total_with_sales_tax(self):
        cart = ShoppingCart()
        cart.add("Item 1", 10)
        cart.add("Item 2", 20)
        total = cart.total(8)
        self.assertAlmostEqual(total, 32.4)

    def test_total_without_sales_tax(self):
        cart = ShoppingCart()
        cart.add("Item 1", 10)
        cart.add("Item 2", 20)
        total = cart.total(0)
        self.assertEqual(total, 30.0)


class TestShoppingCart2(unittest.TestCase):
    def setUp(self):
        self.cart = ShoppingCart().add("tuna sandwich", 15.00)

    def tearDown(self):
        del self.cart

    def test_length(self):
        self.assertEqual(1, len(self.cart))

    def test_item(self):
        self.assertEqual("tuna sandwich", self.cart.item(1))

    def test_price(self):
        self.assertEqual(15.00, self.cart.price(1))

    def test_total_with_sales_tax(self):
        self.assertAlmostEqual(16.39, self.cart.total(9.25), 2)
