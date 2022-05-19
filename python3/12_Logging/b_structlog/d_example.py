import structlog
class CustomPrintLogger:
    def msg(self, message):
        print(message)
def proc(logger, method_name, event_dict):
    print("I got called with", event_dict)
    return repr(event_dict)
log = structlog.wrap_logger(
    CustomPrintLogger(),
    wrapper_class=structlog.BoundLogger,
    processors=[proc],
)
log2 = log.bind(x=42)
print("log == log2 :", log == log2) # False

log.msg("hello world")
# I got called with {'event': 'hello world'}
# {'event': 'hello world'}
log2.msg("hello world")
# I got called with {'x': 42, 'event': 'hello world'}
# {'x': 42, 'event': 'hello world'}

log3 = log2.unbind("x")
print("log == log2 :", log == log2) # True

log3.msg("hello world")
# I got called with {'event': 'hello world'}
# {'event': 'hello world'}
