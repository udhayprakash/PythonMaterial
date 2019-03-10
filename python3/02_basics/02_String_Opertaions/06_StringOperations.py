print('--------STRING FORMATTING-------')
print('-----OLD STYLE FORMATTING----')
print('' % ())
print('%d' % (12))
# print '%d'%('12')  # TypeError: %d format: a number is required, not str
print('%s' % ('12'))
print('%f' % (12.34))
print('%f' % (12))
print('%s' % (True))
# %d - integer
# %s - string/char
# %f - floating-point

print('lucky number is %d only.' % (786))
print('lucky number is %d only.' % 786)
print('pi value is %f!!!!!!!!!!' % (3.1416))
print('my name is %s - %s.' % ('Udhay', 'Prakash'))

print('My name is %s. I am %d old paying a tax of %f')
print('My name is %s. I am %d old paying a tax of %f' % ('Udhay', 99, 15.5))
print('My name is %r. I am %r old paying a tax of %r' % ('Udhay', 78, 15.5))
# print 'My name is %s. I am %d old paying a tax of %f'%('Udhay', 33 )
  #TypeError: not enough arguments for format string



print('------NEW Style formating------')
print('{}'.format(''))
print('{} and {}'.format('cat', 'mouse'))

print('Name:{} Age:{} Salary:{}'.format('udhay', 99, 9999.9999))

print('''Name  :{} 
         Age   :{} 
         Salary:{}'''.format('udhay', 99, 9999.9999))

print('My Name: {0}. My Name: {0}. My Name: {0}. My Name: {0}. '.format('udhay', 23, 34234))

print('''
        Name  :{2} 
        Age   :{0} 
        Salary:{0}'''.format('udhay', 99, 9999.9999))

print('''
        Name  :{NAME} , Name  :{NAME}
        Age   :{AGE} 
        Salary:{SALARY}'''.format(NAME='udhay', AGE=99, SALARY=9999.9999))


print('f-strings', '='* 20)

name = 'World'
print(f"Hello {name}")
# python operations on data within the f-string 
print(f"Hello {name.upper()}")

value = 123123
print(f'The value is {float(value)}')

NAME='udhay'
AGE=99
SALARY=9999.9999
print(f'''
        Name  :{NAME} , Name  :{NAME}
        Age   :{AGE} 
        Salary:{SALARY}''')