import logging
import time

import requests
import sentry_sdk
from sentry_sdk.integrations.logging import LoggingIntegration

# Initialize Sentry
sentry_logging = LoggingIntegration(
    level=logging.INFO,  # Specify the logging level for capturing messages
    event_level=logging.ERROR,  # Specify the logging level for capturing events as errors
)
sentry_sdk.init(
    dsn="https://97dc0bd32b604a14a4bed51235b0d213@o386823.ingest.sentry.io/4505459696599040",
    integrations=[sentry_logging],
    # Setting to 1.0 will capture 100% of transactions for performance monitoring
    traces_sample_rate=1.0,
)

# Example 1: Basic Exception Logging
try:
    # Code that may raise an exception
    raise ValueError("An error occurred!")
except Exception as e:
    sentry_sdk.capture_exception(e)

# Example 2: Logging Caught Exceptions
try:
    # Code that may raise an exception
    raise ValueError("An error occurred!")
except Exception as e:
    logging.error("Caught an exception: %s", str(e))
    sentry_sdk.capture_exception(e)

# Example 3: Custom Logging Messages
sentry_sdk.capture_message("This is a custom log message")

# Example 4: Error Aggregation
for i in range(5):
    try:
        # Code that may raise an exception
        raise ValueError("An error occurred!")
    except Exception as e:
        sentry_sdk.capture_exception(e)

# Example 5: Contextual Information
try:
    # Code that may raise an exception
    raise ValueError("An error occurred!")
except Exception as e:
    with sentry_sdk.configure_scope() as scope:
        scope.set_user({"id": 123, "username": "john.doe"})
        scope.set_extra("request_id", "abcd1234")
        sentry_sdk.capture_exception(e)

# Example 6: Error Severity Levels
try:
    # Code that may raise an exception
    raise ValueError("A warning occurred!")
except Exception as e:
    sentry_sdk.capture_exception(e, level="warning")

# Example 7: Performance Monitoring
with sentry_sdk.start_transaction(op="transaction_name") as transaction:
    try:
        start_time = time.time()
        # Code to measure performance
        time.sleep(1)  # Simulating some work
        end_time = time.time()
        elapsed_time = end_time - start_time

        # Attach performance data to the transaction
        transaction.set_data("elapsed_time", elapsed_time)

        # Optionally, you can capture an error or log message within the transaction
        if elapsed_time > 2:
            sentry_sdk.capture_message("Performance took too long")

    except Exception as e:
        sentry_sdk.capture_exception(e)

# Example 8: Integration with Logging Libraries
logger = logging.getLogger(__name__)
logger.addHandler(sentry_logging._handler)
logger.error("An error occurred!")


# Example 9: Tracking HTTP requests:
def get_weather_info():
    response = requests.get(
        "https://api.openweathermap.org/data/2.5/weather?q=London&appid=YOUR_API_KEY"
    )

    # Attach the HTTP request data to the transaction
    with sentry_sdk.start_transaction(op="request", request=response):
        weather_info = response.json()

    return weather_info


# Example 10: Customizing Sentry configuration
sentry_sdk.init(
    dsn="",
    environment="production",
    release="1.0.0",
    send_default_pii=True,
)
