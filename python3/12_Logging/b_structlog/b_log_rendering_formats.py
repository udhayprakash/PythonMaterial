import structlog

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

# TODO
# structlog.processors.StackInfoRenderer()
# structlog.processors.ExceptionRenderer()
