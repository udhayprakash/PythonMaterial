#!/usr/bin/python
"""
Purpose:
"""

def person_lister(f):
    def inner(people):
        #print people
        for p in sorted(people, key= lambda x:x[2]):
            print(" ".join(['Mr.' if p[-1] == 'M' else 'Ms.',p[0], p[1]]))
    return inner

@person_lister
def name_format(person):
	return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
	people = [input().split() for i in range(int(input('Enter input:')))]
	print('\n'.join(name_format(people)))
