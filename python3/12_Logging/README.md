## Logging

Logging serves two purposes: 1. Diagnostic logging - This logging records events related to the application's operation. - If a user calls in to report an error, for example, the logs can be searched for context. 2. Audit logging - Audit logging records events for business analysis. - A user’s transactions (such as a clickstream) can be extracted and combined with other user
details (such as eventual purchases) for reports or to optimize a business goal.

```log
    20-July,2015 7.40am     [info	] 	[functionName1] started installing the product
    20-July,2015 7.41am     [debug	]	[functionName2] Installing the prerequisites
    20-July,2015 7.41am     [info	]	[functionName2]	installing the core software
    20-July,2015 7.42am     [debug	]	[functionName3]	reconfigure the machine setting
    20-July,2015 7.43am     [info]		[ main  	  ]	Successfully installed the product
    20-July,2015 7.42am     [error   ]	[functionName3]	unable to reconfigure the machine setting
    20-July,2015 7.42am     [warning ]	[functionName3]	retrying to reconfigure ...
    20-July,2015 7.42am     [critical]	[functionName3]	unable to reconfigure the machine setting
    20-July,2015 7.43am     [critical]  [ main        ]	ABORTED installing the product
```

print ---
SDLC ( dev -> testing/ UAT -> Prod)
debug developement
info dev/testing
warning dev/testing
error dev/testing/prod
critical dev/testing/prod

## Logging Handlers

1. StreamHandler instances send messages to streams (file-like objects).
2. FileHandler instances send messages to disk files.
3. BaseRotatingHandler is the base class for handlers that rotate log files at a certain point.
   It is not meant to be instantiated directly.
   Instead, use RotatingFileHandler or TimedRotatingFileHandler.
   a) RotatingFileHandler instances send messages to disk files, with support for maximum log file sizes and log file rotation.
   b) TimedRotatingFileHandler instances send messages to disk files, rotating the log file at certain timed intervals.
4. SocketHandler instances send messages to TCP/IP sockets.
5. DatagramHandler instances send messages to UDP sockets.
6. SMTPHandler instances send messages to a designated email address.
7. SysLogHandler instances send messages to a Unix syslog daemon, possibly on a remote machine.
8. NTEventLogHandler instances send messages to a Windows NT/2000/XP event log.
9. MemoryHandler instances send messages to a buffer in memory, which is flushed whenever specific criteria are met.
10. HTTPHandler instances send messages to an HTTP server using either GET or POST semantics.
11. WatchedFileHandler instances watch the file they are logging to.
    If the file changes, it is closed and reopened using the file name.
    This handler is only useful on Unix-like systems; Windows does not support the underlying mechanism used.
12. NullHandler instances do nothing with error messages.
    They are used by library developers who want to use logging, but want to avoid the “No handlers could be found for logger XXX” message which can be displayed if the library user has not configured logging.
