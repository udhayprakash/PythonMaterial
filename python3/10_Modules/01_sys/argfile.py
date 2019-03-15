# import time
# for i in range(90):
#     time.sleep(1)  # 1sec 
# name = input('name=')
# print 'Entered named is', name


import sys

# print('__file__', __file__)
# print('sys.argv', sys.argv, type(sys.argv))

# if len(sys.argv) == 1:
#     print('Enter properly')
#     print(__file__, 'name')
#     sys.exit(0)
    
# name = sys.argv[1]
# print('Entered name is', name)


# sys.argv

print("sys.argv     :", sys.argv)
print("len(sys.argv):", len(sys.argv))

winningTicket = '123Alpha'

if len(sys.argv) == 1:
    print('Please enter the ticket number\n')
    print('USAGE:')
    print('      python argfile.py 231asdas')
    print('__file__ :', __file__)
    print('      python', __file__, '231sads')
    sys.exit(1)

userEnteredTicket = sys.argv[1]

if winningTicket == userEnteredTicket:
    print('You won the lottery')
else:
    print('You Lost. Try again!')


