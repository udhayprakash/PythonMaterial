import threading
from unittest import TestCase

from django.urls import reverse


def test_concurrently(times):
    """
    Add this decorator to small pieces of code that you want to test
    concurrently to make sure they don't raise exceptions when run at the
    same time.  E.g., some Django views that do a SELECT and then a subsequent
    INSERT might fail when the INSERT assumes that the data has not changed
    since the SELECT.
    """

    def test_concurrently_decorator(test_func):
        def wrapper(*args, **kwargs):
            exceptions = []

            def call_test_func():
                try:
                    test_func(*args, **kwargs)
                except Exception as e:
                    exceptions.append(e)
                    raise

            threads = []
            for _ in range(times):
                threads.append(threading.Thread(target=call_test_func))
            for t in threads:
                t.start()
            for t in threads:
                t.join()
            if exceptions:
                raise Exception(
                    "test_concurrently intercepted %s exceptions: %s"
                    % (len(exceptions), exceptions)
                )

        return wrapper

    return test_concurrently_decorator


class Client:
    pass


class MyTestCase(TestCase):
    def testRegistrationThreaded(self):
        url = reverse("toggle_registration")

        @test_concurrently(15)
        def toggle_registration():
            # perform the code you want to test here; it must be thread-safe
            # (e.g., each thread must have its own Django test client)
            c = Client()
            c.login(username="user@example.com", password="abc123")
            response = c.get(url)
            print(response)

        toggle_registration()
