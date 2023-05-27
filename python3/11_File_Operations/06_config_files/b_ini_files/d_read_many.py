from configparser import ConfigParser

parser = ConfigParser()


candidates = (
    "does_not_exist.ini",
    "also-does-not-exist.ini",
    "simple.ini",
    "multisection.ini",
)
found = parser.read(candidates)
print(found)

missing = set(candidates) - set(found)

print("Found config files:", sorted(found))
print("Missing files     :", sorted(missing))
