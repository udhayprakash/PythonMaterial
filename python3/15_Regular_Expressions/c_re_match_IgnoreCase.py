"""
Purpose: Regular Expressions
    Using re.match
        - It helps to identify patterns at the starting of string
        - By default, it is case-sensitive

    Flags can modify the pattern behaviour
        re.I/ re.IGNORECASE  will help to perform case-insensitive pattern matches
"""
import re

target_string = "Python Programming is good for health"
# search_string = "python"

for search_string in ("python", "Python", "PYTHON", "PYThon"):
    print("\nsearch_string =", search_string)

    # print(f"{target_string.find(search_string) =}")
    # print(f"{search_string in target_string    =}")
    print(f"{target_string.lower().find(search_string.lower()) =}")
    print(f"{search_string.lower() in target_string.lower()    =}")
    print()

    reg_obj = re.compile(search_string, re.I)  # re.IGNORECASE
    print(reg_obj, type(reg_obj))

    result = reg_obj.match(target_string)
    print(f"{result =}")

    if result:
        print(f"result.group():{result.group()}")
        print(f"result.span() :{result.span()}")
        print(f"result.start():{result.start()}")
        print(f"result.end()  :{result.end()}")
    else:
        print("NO match found")
