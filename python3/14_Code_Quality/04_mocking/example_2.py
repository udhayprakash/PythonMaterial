from unittest import main, TestCase
from unittest.mock import Mock


def can_cancel_order(order_id, shipping_system):
    status = shipping_system.get_status(order_id)
    if status in ("SENT", "DELIVERED"):
        return False
    return True


class CanCancelOrderTest(TestCase):
    def test_can_cancel_order_with_status_sent_false(self):
        order_id = 1
        shipping_system_mock = Mock(get_status=Mock(return_value="SENT"))

        result = can_cancel_order(1, shipping_system_mock)

        self.assertFalse(result)


if __name__ == "__main__":
    main()
