#!/usr/bin/python
"""
Purpose: Context Manager
"""
# context mangers

# Method 1
f = open("31_context_manager.txt", "w")
f.write("I am good")
f.close()

# Method 2
with open("31_context_manager.txt", "w") as f:
    f.write("I am good")

##############################################


class ManagedFile:
    def __init__(self, file_name, mode="r"):
        self.name = file_name
        self.file_operation_mode = mode

    def __repr__(self):
        return f"{self.name} in {self.file_operation_mode}"

    def __enter__(self):
        self.file = open(self.name, self.file_operation_mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()


# f1 = ManagedFile('31_context_manager.txt', 'w')
# print(f1)


with ManagedFile("31_context_manager.txt", "w") as f1:
    print(f1)
    f1.write("I am good")


###########################################################
class CM:
    def __enter__(self):
        print("Raing Erro 1")
        raise OSError()
        return self

    def __exit__(self, exc_type, exc_val, exc_tab):
        pass


c = CM()
with c:
    try:
        print("raining valueError2")
        raise ValueError()
    except ValueError:
        print("excepty caght")
