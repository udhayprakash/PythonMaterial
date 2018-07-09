#!/usr/bin/python
"""
Purpose: Multiline statements


\ line continuation operator

()

[]
{}
"""

sumOfValues = 12 + 45 + 34534545 + 343 - 34234 + \
              34 + 454 + 42534 + 34 / 34 + 34534 \
              + 34234 + 67 + 454 - 435 - 43534

print 'sumOfValues:', sumOfValues

# , logic separation operator


sumOfValues = (12 + 45 + 34534545 + 343 - 34234 +
               34 + 454 + 42534 + 34 + 34 + 34534
               + 34234 + 67 + 454 - 435 - 43534)

print 'sumOfValues:', sumOfValues

sumOfValues = [12 + 45 + 34534545 + 343 - 34234 +
               34 + 454 + 42534 + 34 + 34 + 34534
               + 34234 + 67 + 454 - 435 - 43534]

print 'sumOfValues:', sumOfValues

