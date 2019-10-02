# # context mangers

# Method 1
f = open('hello.txt', 'w')
f.write('I am good')
f.close()

# Method 2
with open('hello.txt', 'w') as f:
    f.write('I am good')
    f.close()


# f.write('asdasd')

##############################################
class ManagedFile:
    def __init__(self, file_name, mode='r'):
        self.name = file_name
        self.file_operation_mode = mode

    def __enter__(self):
        self.file = open(self.name, self.file_operation_mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()


with ManagedFile('hello.txt', 'w') as f:
    f.write('I am good')
    f.close()
