import os 
import subprocess

command_to_execute = 'ping -n 4 www.google.com'
command_to_execute = 'dir /x'

# result = os.system(command_to_execute)
# print(f'result:{result}')


p = subprocess.Popen(command_to_execute, 
            stdout=subprocess.PIPE, 
            stderr=subprocess.PIPE)
output, err = p.communicate()


breakpoint()
print(output.decode('utf-8'))
print(err.decode('utf-8'))