"""
Purpose: Python Disassembler

    To print the assembly code for the python code


    ONLINE TOOL - https://www.dis-this.com/
"""

import dis


def hello():
    print("Hello world")


print(dis.dis(hello))
print("-" * 20)


def hello2(name):
    print("Hello %", name)
    print("Hello {}".format(name))
    print(f"Hello {name}")


print(dis.dis(hello2))


# bytecode analyses

bytecode = dis.Bytecode(hello2)
for instr in bytecode:
    print(instr.opname)
