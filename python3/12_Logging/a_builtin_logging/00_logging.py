import sys

print("This is print message")
sys.stderr.write("This is sys.stderr write message\n")
sys.stdout.write("This is sys.stdout write message\n")
print()

f = open("logs/00_print_log.log", "w")
print("print() function - with file handler", file=f, flush=True)
fh.close()

fh = open("00_print_log.log", "a")
print("print() function - with file handler 22", file=fh, flush=True)
# fh.close()

# To make all further prints to go to file
sys.stdout = f
sys.stderr.write("This is sys.stderr write message\n")
sys.stdout.write("This is sys.stdout write message\n")
print("print() function - ordinary1")
print("print() function - ordinary2")
print("print() function - ordinary3")
print(None, True, False, -2131.122, 1212)
print([12, 12, 23, (2323, {4, 5})])


try:
    1 + "1"
except Exception as ex:
    print(ex)

sys.stderr = f
1 / 0

f.close()
print("Last statement")  # will not execute
