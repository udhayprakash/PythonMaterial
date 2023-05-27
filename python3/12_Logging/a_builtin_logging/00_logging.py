import os
import sys

os.makedirs("logs", exist_ok=True)


print("This is print message")
sys.stderr.write("This is sys.stderr write message\n")
sys.stdout.write("This is sys.stdout write message\n")
print()

fh = open("logs/00_print_log.log", "w")
print("print() function - with file handler", file=fh, flush=True)
fh.close()

fh = open("logs/00_print_log_append.log", "a")
print("print() function - with file handler", file=fh, flush=True)
# fh.close()

# To make all further prints to go to file
sys.stdout = fh

sys.stderr.write("This is sys.stderr write message2\n")
sys.stdout.write("This is sys.stdout write message2\n")
print("print() function - ordinary1")
print("print() function - ordinary2")
print("print() function - ordinary3")
print(None, True, False, -2131.122, 1212)
print([12, 12, 23, (2323, {4, 5})])


try:
    1 + "1"
except Exception as ex:
    print(ex)


sys.stderr = fh
1 / 0

fh.close()
print("Last statement")  # will not execute
