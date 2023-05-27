import configparser

p1 = configparser.ConfigParser()
p1.read("simple.ini")

print(p1.has_section("bug_tracker"))

for candidate in ("bug_tracker", "wiki"):
    print(candidate, p1.has_section(candidate))

print()


p2 = configparser.ConfigParser()
p2.read("multisection.ini")

for candidate in ("bug_tracker", "wiki"):
    print(candidate, p2.has_section(candidate))
