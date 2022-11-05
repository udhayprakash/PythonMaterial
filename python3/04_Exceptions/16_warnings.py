#!/usr/bin/python3
"""
Purpose: Handling warnings
"""
import warnings

for each_attribute in dir(warnings):
    if not each_attribute.startswith("_"):
        print(each_attribute)
print()

warnings.warn("This is not good practice 1")

# Adding filter to display on specific warnings
warnings.filterwarnings(
    "ignore",
    ".*do not.*",
)

warnings.warn("This warning will be displayed")
warnings.warn("Do not show this message")
print()

try:
    # To throw exception when error warning is present
    warnings.simplefilter("error", UserWarning)
    warnings.warn("This is not good practice 2")
except UserWarning as ex:
    print(repr(ex))
except Exception as ex:
    print("Unhandled Exception", repr(ex))
