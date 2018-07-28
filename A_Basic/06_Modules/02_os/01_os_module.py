import os 
print os.path.basename("/home/user/temp.txt")  # temp.txt
print os.path.dirname("/home/user/temp.txt")   # /home/user
print os.path.abspath('temp.txt')              # /home/user/temp.txt
print os.path.realpath("/home/user/temp.txt")
print
print os.path.splitext("/home/user/temp.log")  # ('/home/user/temp', '.log')
print os.path.splitdrive("/home/user/temp.txt")  # ('', '/home/user/temp.txt')
print os.path.extsep                            # .
print os.sep                                    # /
print 

print os.getcwd()

fd = "GFG.txt"
os.rename(fd,'New.txt')
os.rename(fd,'New.txt')
