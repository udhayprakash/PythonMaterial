"""
Purpose: Look assertion

        1) Positive Lookahead   (?=...)
            - Matches if the pattern inside the lookahead assertion is present ahead.
            - Ex: apple(?= pie) matches "apple" only if it is followed by the word "pie".

        2) Negative Lookahead   (?!...)
            - Matches if the pattern inside the lookahead assertion is not present ahead.
            - Ex: apple(?! pie) matches "apple" only if it is not followed by the word "pie".

        3) Positive Lookbehind   (?<=...)
            - Matches if the pattern inside the lookbehind assertion is present behind.
            - Ex: (?<=good )morning matches "morning" only if it is preceded by the word "good".

        4) Negative Lookbehind   (?<=...)
            - Matches if the pattern inside the lookbehind assertion is not present behind.
            - Ex: (?<!not )good morning matches "good morning" only if it is not preceded by the word "not".

"""
import re

print(re.findall("apple", "I love apple pie, but not apple juice or apple cider."))

print("\nPositive LookAhead")
print(
    re.findall(
        r"apple(?=\s+pie)",  # 'apple' followed by one or more whitespaces, then 'pie'
        "I love apple pie, but not apple juice or apple cider.",
    )
)
print(
    re.findall(
        r"\w+(?=\d+)",
        "apple apple123 ball ball3 cat45.5 dog",
    )
)

print("\nNegative LookAhead")
print(
    re.findall(
        r"apple(?!.*pie)",  # 'apple' NOT followed by 'pie'
        "I love apple pie, but not apple juice or apple cider.",
    )
)
print(
    re.findall(
        r"\w+(?!\d+)",
        "apple apple123 ball ball3 cat45.5 dog",
    )
)


print("\nLookahead with Capturing Group")
print(
    re.findall(
        r"(\w+)(?=!)",  # captures words followed by !, but gets only words
        "Hello! How are you? Fine!",
    )
)

emails = ["example1@gmail.com", "example2@yahoo.com", "example3@hotmail.com"]
pattern = r"@(\w+)(?=\.\w+$)"
domains = [re.search(pattern, email).group(1) for email in emails]
print(domains)

timestamps = ["12:34:56", "09:45:23", "21:15:10"]
pattern = r"(\d+)(?=:)"
hours = [re.search(pattern, timestamp).group(1) for timestamp in timestamps]
print(hours)

urls = [
    "https://www.example.com/home",
    "https://www.example.com/products",
    "https://www.example.com/about",
]
pattern = r"(/[^/]+)(?=\b|$)"
paths = [re.search(pattern, url).group(1) for url in urls]
print(paths)
print()

# ------------------------------------------------
print("\nPositive lookbehind assertion (?<=...)")
result = re.findall(r"(?<=I love )\w+", "I love Python")
print(result)

print("\nNegative lookbehind assertion (?<!...)")
result = re.findall(r"\b(?<!not )\w+\b", "I love Python, but not Java")
print(result)
print()

# ------------------------------------------------
# Matching the same text as a named group (?P=name):

print(re.findall(r"(?P<word>\w+)\s(?P=word)", "apple apple apple"))
print(re.findall(r"(?P<word>\w+)\s(?P=word)", "Hello Hello World World"))

text = """
    Server IP: 192.168.0.1, Client IP: 10.0.0.1
    Server IP: 192.168.0.2, Client IP: 192.168.0.2
    Server IP: 10.0.0.1, Client IP: 10.0.0.1
"""
pattern = r"Server IP: (?P<server_ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}), Client IP: (?P=server_ip)"
results = re.findall(pattern, text)
print(results)
