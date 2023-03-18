import structlog

log = structlog.get_logger()

log.msg("first message")
log.info("first message")

log.msg("second message", whom="world", more_than_a_string=[1, 2, 3])
log.info("second message", whom="world", more_than_a_string=[1, 2, 3])

log.msg("third message", key="value!", more_than_strings=[1, 2, 3])
log.info("third message", key="value!", more_than_strings=[1, 2, 3])

"""
2023-03-17 12:16:24 [info     ] first message
2023-03-17 12:16:24 [info     ] first message
2023-03-17 12:16:24 [info     ] second message                 more_than_a_string=[1, 2, 3] whom=world     2023-03-17 12:16:24 [info     ] second message                 more_than_a_string=[1, 2, 3] whom=world
2023-03-17 12:16:24 [info     ] third message                  key=value! more_than_strings=[1, 2, 3]      2023-03-17 12:16:24 [info     ] third message                  key=value! more_than_strings=[1, 2, 3]

"""
