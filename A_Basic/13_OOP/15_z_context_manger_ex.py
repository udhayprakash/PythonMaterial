# context mangers

class ManagedFile:
    def __init__(self, name, mode= 'r'):
        self.name = name
        self.file_operation_mode =  mode

    def __enter__(self):
        self.file = open(self.name, self.file_operation_mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()


with ManagedFile('hello.txt', 'w') as f:
    f.write('Hello world!')