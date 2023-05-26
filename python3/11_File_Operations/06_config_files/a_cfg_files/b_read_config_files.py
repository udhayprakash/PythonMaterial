import configparser

config = configparser.RawConfigParser()
config.read("example.cfg")

# print(config)
# print(dir(config))


# getfloat() raises an exception if the value is not a float
# getint() and getboolean() also do this for their respective types
a_float = config.getfloat("Section1", "a_float")
print(f"{type(a_float)} {a_float}")

an_int = config.getint("Section1", "an_int")
print(f"{type(an_int)} {an_int}")

print(a_float + an_int)
print()

# Notice that the next output does not interpolate '%(bar)s' or '%(baz)s'.
# This is because we are using a RawConfigParser().
if config.getboolean("Section1", "a_bool"):
    print(config.get("Section2", "foo"))
