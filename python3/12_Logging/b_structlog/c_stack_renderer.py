import structlog

print("\n\t structlog.processors.StackInfoRenderer()")
# StackInfoRenderer processor adds information about the call stack,
import structlog


def foo():
    bar()


def bar():
    baz()


def baz():
    log = structlog.get_logger()
    log.error("Here's some info")


structlog.configure(
    processors=[
        structlog.processors.TimeStamper(fmt="iso"),
        structlog.processors.StackInfoRenderer(),
        structlog.processors.JSONRenderer(),
    ],
    logger_factory=structlog.stdlib.LoggerFactory(),
    wrapper_class=structlog.stdlib.BoundLogger,
    context_class=dict,
    cache_logger_on_first_use=True,
)

foo()
