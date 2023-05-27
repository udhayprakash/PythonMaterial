from configparser import ConfigParser

parser = ConfigParser()
parser.read("multisection.ini")
print(parser.sections())

parser.read("types.ini")
print(parser.sections())
print("=====================================\n")


for section_name in parser.sections():
    print("Section:", section_name)
    print("  Options:", parser.options(section_name))
    for name, value in parser.items(section_name):
        print(f"{name} ={value}")
    print()
