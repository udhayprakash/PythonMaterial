import tarfile

# creating files 
open('fileOne.txt', 'w')
open('fileTwo.txt', 'w')
open('fileThree.txt', 'w')

# Creating new archives
with tarfile.open('tarFileOne.tar', mode = 'w') as tF:
    tF.add('fileOne.txt')
    tF.add('fileTwo.txt')

# Appending to existing archive
with tarfile.open('tarFileOne.tar', mode = 'a') as tF:
    tF.add('fileThree.txt')

# deleting existing files 
import os 
os.remove('fileOne.txt')
os.remove('fileTwo.txt')
os.remove('fileThree.txt')

# Extracting a specific file from archive
with tarfile.open('tarFileOne.tar') as tF:
    tF.extract('fileThree.txt')

# Extracting all files in archive
with tarfile.open('tarFileOne.tar') as tF:
    tF.extractall()