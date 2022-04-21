# 04_pdb_example.py

import pdb

# new style classes
class ExampleClass(object):

    def __init__(self, name, number):
        self.name = name
        self.number = number

    def example_entry(self):
        pdb.set_trace()
        return 'The example name is {0} with the number {1}'.format(self.name, self.number)


if __name__ == '__main__':
    example = ExampleClass('Carla', 456)
    print dir(example)
    example.example_entry()
