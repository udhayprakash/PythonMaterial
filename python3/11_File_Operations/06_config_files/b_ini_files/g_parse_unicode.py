import codecs
from configparser import ConfigParser

parser = ConfigParser()

# Open the file with the correct encoding
with codecs.open("unicode.ini", "r", encoding="utf-8") as f:
    parser.readfp(f)

password = parser.get("bug_tracker", "password")

print("Password:", password.encode("utf-8"))
print("Type    :", type(password))
print("repr()  :", repr(password))
