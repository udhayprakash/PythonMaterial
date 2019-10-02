largest = None
print('Before :', largest)
for iterval in [3, 41, 12, 9, 74, 15]:
    if largest == None or largest < iterval:
        largest = iterval
    print(f'Loop   : {iterval:2} {largest:2}')
print(f'Largest: {largest:2}')
