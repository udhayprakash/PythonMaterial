from unittest import TestCase, expectedFailure, mock

from pricing import Pricer


class TestClassAttribute(TestCase):
    def test_patch_instance_attribute(self):
        pricer = Pricer()
        pricer.DISCOUNT = 0.5
        self.assertAlmostEqual(pricer.get_discounted_price(100), 50.0)

    def test_set_class_attribute(self):
        Pricer.DISCOUNT = 0.75
        pricer = Pricer()
        self.assertAlmostEqual(pricer.get_discounted_price(100), 75.0)

    @expectedFailure  # (" There is no PERCENTAGE attribute")
    def test_patch_incorrect_class_attribute(self):
        with mock.patch.object(Pricer, "PERCENTAGE", 1):
            pricer = Pricer()
            self.assertAlmostEqual(pricer.get_discounted_price(100), 100)

    def test_patch_correct_class_attribute(self):
        with mock.patch.object(Pricer, "DISCOUNT", 1):
            pricer = Pricer()
            self.assertAlmostEqual(pricer.get_discounted_price(100), 100)

        self.assertAlmostEqual(pricer.get_discounted_price(100), 75)
