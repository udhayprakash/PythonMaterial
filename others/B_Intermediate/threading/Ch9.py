# These examples are not in individual functions in the chapter, but
# to isolate them, they are separated into individual functions here

def lambda_sample():
    # use lambda with filter
    filter_me = [1, 2, 3, 4, 6,7 ,8, 11, 12, 14, 15, 19, 22]
    # This will only return true for even numbers (because x%2 is 0, or False,
    # for odd numbers)
    result = filter(lambda x: x%2 == 0, filter_me)
    print result


def lambda_named_sample():
    # use lambda with filter, but bind it to a name
    filter_me = [1, 2, 3, 4, 6,7 ,8, 11, 12, 14, 15, 19, 22]
    # This will only return true for even numbers (because x%2 is 0, or False,
    # for odd numbers)
    func = lambda x: x%2 == 0
    result = filter(func, filter_me)
    print result


def reduce_sample():
    # Use reduce with a lambda function to make small numbers into a
    # very big number
    reduce_me = [ 2, 4, 4, 2, 6 ]
    result = reduce(lambda first, second: first**second, reduce_me)
    print "The result of reduce is: %d" % result


def map_sample():
    # Now map gets to be run in the simple case
    map_me = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g' ]
    result = map(lambda x: "The letter is %s" % x, map_me)
    print result


def list_comprehension_sample():
    # First, just print even numbers
    everything = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 ]
    print [ x for x in everything if x%2 == 0 ]

def range_sample():
    # First an example of a range between two numbers
    list = range (10, 20)
    print list

    # range works differently with only one parameter
    for number in range(10):
        print "Number is now %d" % number

    # Using a stride
    for number in range(5, 55, 4):
        print "Number from 5 to 55, by fours: %d" % number

    # xrange provides a special case useful for large sets.
    # In this case, it's overkill, but you can see it works the same way.
    for r in xrange(0, 10):
        print r


def string_substitution_sample():
    person = {"name": "James", "camera": "nikon", "handedness": "lefty", "baseball_team": "angels", "instrument": "guitar"}

    print "%(name)s, %(camera)s, %(baseball_team)s" % person

    person["height"] = 1.6
    person["weight"] = 80
    print "%(name)s, %(camera)s, %(baseball_team)s, %(height)2.2f, %(weight)2.2f" % person    

    # An alternative way to perform these substitutions
    import string
    person = {"name": "James", "camera": "nikon", "handedness": "lefty", "baseball_team": "angels", "instrument": "guitar"}
    person["height"] = 1.6
    person["weight"] = 80
    t = string.Template("$name is $height m high and $weight kilos")
    print t.substitute(person)


def getopt_sample():
    import sys
    import getopt
    # Remember, the first thing in the sys.argv list is the name of the command
    # You don't need that.
    cmdline_params = sys.argv[1:]

    opts, args = getopt.getopt(cmdline_params, 'hc:', ['help', 'config='])
    print opts, args

    for option, parameter in opts:
   
        if option == '-h' or option == '--help':
            print "This program can be run with either -h or --help for this message,"
            print "or with -c or --config=<file> to specify a different configuration file"
            print
        if option in ('-c', '--config'): # this means the same as the above
            print "Using configuration file %s" % parameter

def gnu_getopt_sample():
    import sys
    import getopt
    # Remember, the first thing in the sys.argv list is the name of the command
    # You don't need that.
    cmdline_params = sys.argv[1:]

    opts, args = getopt.gnu_getopt(cmdline_params, 'hc:', ['help', 'config='])
    print opts, args

    for option, parameter in opts:
   
        if option == '-h' or option == '--help':
            print "This program can be run with either -h or --help for this message,"
            print "or with -c or --config=<file> to specify a different configuration file"
            print
        if option in ('-c', '--config'): # this means the same as the above
            print "Using configuration file %s" % parameter

def fork_sample():
    import os
    pid = os.fork()
    # fork and exec together
    print "second test"
    if pid == 0: # This is the child
        print "this is the child"
        print "I'm going to exec another program now"
        os.execl('/bin/cat', 'cat', '/etc/motd')
    else:
        print "the child is pid %d" % pid
        os.wait()        

def determine_platform_sample():
    import os, sys
    if sys.platform == 'win32':
        print "Running on a windows platform"
        command = "C:\\winnt\\system32\\cmd.exe"
        params = []
    
    if sys.platform == 'linux2':
        print "Running on a Linux system, identified by %s" % sys.platform
        command = '/bin/uname'
        params = ['uname', '-a']

    print "Running %s" % command
    os.spawnv(os.P_WAIT, command, params)


def os_system_sample():
    # Now system
    if sys.platform == 'win32':
        print "Running on a windows platform"
        command = "cmd.exe"

    if sys.platform == 'linux2':
        print "Running Linux"
        command = "uname -a"

    os.system(command)


def threading_sample():
    # call the threading module that's here


    
def password_hashing_sample():
    import sha
    import random
    import base64

    def _gen_salt():
        salt = [chr(random.randint(0,255)) for i in range(4) ]
        return ''.join(salt)

    def make_pass(cleartext):
        salt = _gen_salt()
        text = salt + cleartext
        hash = sha.new(text).digest()
        data = salt + hash
        return base64.encodestring(data)

    def check_pass(cipher, cleartext):
        cipher = base64.decodestring(cipher)
        salt, hash = cipher[:4], cipher[4:]
        hash2 = sha.new(salt + cleartext).digest()
        return hash2 == hash

    if __name__ == '__main__':
        cipher = make_pass('TEST')
        for word in 'spam', 'TEST', 'Test', 'omelette':
            passwd = check_pass(cipher, word)
            print '%s: %d' % (word, passwd)    
