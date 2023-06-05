"""
Purpose:

| Network        | IIN (Prefix) | Length |
+----------------+--------------+--------+
|American Express| 34, 37       | 15     |
|Diners Club     | 38, 39       | 14     |

"""
import unittest


def detect_network(card_number):
    """Return the card network for card_number"""
    if len(card_number) == 15 and card_number[:2] in ("34", "37"):
        return "American Express"
    elif len(card_number) == 14 and card_number[:2] in ("38", "39"):
        return "Diners Club"
    return None


class TestDetectNetwork(unittest.TestCase):
    TEST_CASES = [
        ("3412345678901234", "American Express"),
        ("3712345678324234", "American Express"),
        ("381234567890123", "Diners Club"),
        ("391234567867567", "Diners Club"),
        ("3412345678901", None),
        ("37123456789015", None),
    ]

    def test_cases(self):
        for card_number, expected in self.TEST_CASES:
            actual = detect_network(card_number)
            error_msg = (
                f"Card number {card_number} should be {expected} but was {actual}"
            )
            self.assertEqual(actual, expected, error_msg)


if __name__ == "__main__":
    unittest.main(exit=False)
