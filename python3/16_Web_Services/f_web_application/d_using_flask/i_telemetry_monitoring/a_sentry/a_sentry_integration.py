"""
Purpose: Flask app with sentry integration
    1. create sentry account
    2. create a flask project in it
    3. Get the DSN and copy in code

    pip install --upgrade 'sentry-sdk[flask]'

"""
import sentry_sdk
from flask import Flask
from sentry_sdk.integrations.flask import FlaskIntegration

# Configure Flask app
app = Flask(__name__)

# Configure Sentry
sentry_sdk.init(
    dsn="https://4990dbc96cc34e72a1e0045ae45141bf@o386823.ingest.sentry.io/4505460829257728",
    integrations=[FlaskIntegration()],
    traces_sample_rate=1.0,
)


@app.route("/debug-sentry")
def trigger_error():
    division_by_zero = 1 / 0


if __name__ == "__main__":
    app.run(debug=True)
