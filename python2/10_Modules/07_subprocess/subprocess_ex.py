import subprocess

command_to_execute = 'dir /x'.split(' ')
print 'subprocess.call=========='
print subprocess.call(command_to_execute)


print 'subprocess.Popen=========='
p = subprocess.Popen(command_to_execute)
print p.communicate()

p = subprocess.Popen(command_to_execute, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
print p.communicate()

args = 'ping -c 4 www.google.com'.split(' ')
p = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
print p.communicate()
