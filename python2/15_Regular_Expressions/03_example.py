import re
print re.match('a{1,2}?shique', 'aashique').group()
print re.search('a{1,2}?shique', 'aashique').group()

print re.match('a{1,2}?shique', 'ashique').group()
print re.search('a{1,2}?shique', 'ashique').group()



print re.search('a{1,2}?shique', 'aaaaashique').group()


print re.search('a{1,2}?', 'aaaaa').group()
print re.search('a{1,2}', 'aaaaa').group()

print '-----------'

print re.match(r'(..)*', 'alb2cs').group(1)
print re.match(r'(..)+', 'alb2cs').group(1)
print re.match(r'(..)?', 'alb2cs').group(1)
