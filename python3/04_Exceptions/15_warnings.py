#!/usr/bin/python3
"""
Purpose: Handling Warnings 


"""
import warnings

# print(dir(warnings))

warnings.warn('This is not good practice 1')
print()

# Adding filter to display on specific warnings
warnings.filterwarnings('ignore', '.*do not.*', )

warnings.warn('This warning will be displayed')
warnings.warn('Do not show this message')
print()

try:
    # To throw exception when error warning is present
    warnings.simplefilter('error', UserWarning)
    warnings.warn('This is not good practice 2')
except UserWarning as ex:
    print(repr(ex))
except Exception as ex:
    print('Unhandled Exception', repr(ex))
print()
