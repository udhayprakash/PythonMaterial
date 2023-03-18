import structlog

print("\n\t DEFAULT Renderer")

log = structlog.get_logger()
log.msg("first message")
log.msg("second message", whom="world", more_than_a_string=[1, 2, 3])
log.msg("third message", key="value!", more_than_strings=[1, 2, 3])
"""
2023-03-17 12:18:16 [info     ] first message
2023-03-17 12:18:16 [info     ] second message                 more_than_a_string=[1, 2, 3] whom=world
2023-03-17 12:18:16 [info     ] third message                  key=value! more_than_strings=[1, 2, 3]
===========================================================================
"""

print("\n\t structlog.processors.KeyValueRenderer()")
structlog.configure(
    processors=[
        structlog.processors.KeyValueRenderer(),
    ],
)

log = structlog.get_logger()
log.msg("first message")
log.msg("second message", whom="world", more_than_a_string=[1, 2, 3])
log.msg("third message", key="value!", more_than_strings=[1, 2, 3])
"""
        structlog.processors.KeyValueRenderer()
event='first message'
whom='world' more_than_a_string=[1, 2, 3] event='second message'
key='value!' more_than_strings=[1, 2, 3] event='third message'
===========================================================================
"""


print("\n\t structlog.processors.JSONRenderer()")
structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(),
    ],
)

log = structlog.get_logger()
log.msg("first message")
log.msg("second message", whom="world", more_than_a_string=[1, 2, 3])
log.msg("third message", key="value!", more_than_strings=[1, 2, 3])
"""
         structlog.processors.JSONRenderer()
{"event": "first message"}
{"whom": "world", "more_than_a_string": [1, 2, 3], "event": "second message"}
{"key": "value!", "more_than_strings": [1, 2, 3], "event": "third message"}
===========================================================================
"""


print("\n\t structlog.processors.LogfmtRenderer()")
structlog.configure(
    processors=[
        structlog.processors.LogfmtRenderer(),
    ],
)

log = structlog.get_logger()
log.msg("first message")
log.msg("second message", whom="world", more_than_a_string=[1, 2, 3])
log.msg("third message", key="value!", more_than_strings=[1, 2, 3])
"""
         structlog.processors.LogfmtRenderer()
event="first message"
whom=world more_than_a_string="[1, 2, 3]" event="second message"
key=value! more_than_strings="[1, 2, 3]" event="third message"
===========================================================================
"""


print("\n\t structlog.processors.ExceptionRenderer()")


def divide(x, y):
    try:
        return x / y
    except Exception as e:
        log = structlog.get_logger()
        log.error("Error occurred while dividing", x=x, y=y, exc_info=e)


structlog.configure(
    processors=[
        structlog.processors.TimeStamper(fmt="iso"),
        structlog.processors.ExceptionRenderer(),
        structlog.processors.JSONRenderer(),
    ],
    logger_factory=structlog.stdlib.LoggerFactory(),
    wrapper_class=structlog.stdlib.BoundLogger,
    context_class=dict,
    cache_logger_on_first_use=True,
)

divide(1, 0)
"""
         structlog.processors.ExceptionRenderer()
{"x": 1, "y": 0, "event": "Error occurred while dividing", "timestamp": "2023-03-17T12:32:01.256253Z", "exception": "Traceback (most recent call last):\n  File \"D:\\MEGAsync\\Python-related\\PythonMaterial\\python3\\12_Logging\\b_structlog\\b_log_rendering_formats.py\", line 81, in divide\n    return x / y\n           ~~^~~\nZeroDivisionError: division by zero"}
===========================================================================
"""
