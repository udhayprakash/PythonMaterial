import os
import psutil

print(psutil.cpu_percent())
print(psutil.virtual_memory())  # physical memory usage
print('memory % used:', psutil.virtual_memory()[2])


pid = os.getpid()
python_process = psutil.Process(pid)
memoryUse = python_process.memory_info()[0]/2.**30  # memory use in GB...I think
print('memory use:', memoryUse)

# https://stackoverflow.com/questions/276052/how-to-get-current-cpu-and-ram-usage-in-python
