#!/usr/bin/python
"""
Purpose:
    OpenTelemetry promises to solve this complexity by providing a vendor-agnostic
    standard for observability, allowing users to decouple instrumentation and
    routing from storage and query.

"""
from random import randint

from flask import Flask, request
from opentelemetry import trace
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor, ConsoleSpanExporter

provider = TracerProvider()
processor = BatchSpanProcessor(ConsoleSpanExporter())
provider.add_span_processor(processor)
trace.set_tracer_provider(provider)
tracer = trace.get_tracer(__name__)

# pip install opentelemetry-api opentelemetry-sdk

app = Flask(__name__)


# Method 1 :Traditional
# @app.route("/roll")
# def roll():
#     sides = int(request.args.get('sides'))
#     rolls = int(request.args.get('rolls'))
#     return roll_sum(sides, rolls)


# Method 2 : With Tracing
# @app.route("/roll")
# def roll():
#     with tracer.start_as_current_span("server_request"):
#         sides = int(request.args.get('sides'))
#         rolls = int(request.args.get('rolls'))
#         return roll_sum(sides, rolls)


# def roll_sum(sides, rolls):
#     sum = 0
#     for r in range(0, rolls):
#         result = randint(1, sides)
#         sum += result
#     return str(sum)

# Method 3 : With Tracing
@app.route("/roll")
def roll():
    with tracer.start_as_current_span(
        "server_request", attributes={"endpoint": "/roll"}
    ):

        sides = int(request.args.get("sides"))
        rolls = int(request.args.get("rolls"))
        return roll_sum(sides, rolls)


def roll_sum(sides, rolls):
    span = trace.get_current_span()
    sum = 0
    for r in range(0, rolls):
        result = randint(1, sides)
        span.add_event(
            "log",
            {
                "roll.sides": sides,
                "roll.result": result,
            },
        )
        sum += result
    return str(sum)


if __name__ == "__main__":
    app.run(debug=True, port=8081)


# curl "http://127.0.0.1:8081/roll?sides=10&rolls=1"
