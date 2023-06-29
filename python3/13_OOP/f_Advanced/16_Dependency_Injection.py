"""
Purpose: Dependency Injection
    - Design Pattern
    - Allows objects to be loosely coupled
    - promotes code reusability, testability and flexibility
    - In Python, DI is achieved using constructor injection or setter injection

"""

# ---METHOD 1------- Dependency Injection Through constructor injection


class EmailService:
    def send_email(self, recipient, message):
        print(f"Sending email to {recipient}: {message}")


class OrderProcessor:
    def __init__(self, email_service):
        self.email_service = email_service

    def process_order(self, order):
        # Process the order logic
        self.email_service.send_email(
            order.customer_email, "Your order has been processed."
        )


class Order:
    def __init__(self, customer_email):
        self.customer_email = customer_email


# Usage
email_service = EmailService()
order = Order("customer@example.com")
order_processor = OrderProcessor(email_service)  # Constructor injection
order_processor.process_order(order)

"""
Explanation:

    The OrderProcessor class depends on an instance of the EmailService class to send emails.
    Instead of creating an instance of EmailService within the OrderProcessor class, we inject it through the constructor.
    This allows the OrderProcessor class to be decoupled from the EmailService implementation, making it easier to
    substitute different email services or mock the dependency during testing.


"""


# ---METHOD 1------- Dependency Injection Through Setter injection


class EmailService:
    def send_email(self, recipient, message):
        print(f"Sending email to {recipient}: {message}")


class OrderProcessor:
    def set_email_service(self, email_service):
        self.email_service = email_service

    def process_order(self, order):
        # Process the order logic
        self.email_service.send_email(
            order.customer_email, "Your order has been processed."
        )


class Order:
    def __init__(self, customer_email):
        self.customer_email = customer_email


# Usage
email_service = EmailService()
order = Order("customer@example.com")
order_processor = OrderProcessor()
order_processor.set_email_service(email_service)  # Setter injection
order_processor.process_order(order)


"""
Explanation:

    Setter injection helps to inject dependencies by allowing us to set them after object creation.
    UseCases
        1) when dependencies are optional or
        2) when can change during the object's lifetime.
    However, it's important to ensure that the dependencies are properly set before using the object to avoid potential runtime errors.

"""
