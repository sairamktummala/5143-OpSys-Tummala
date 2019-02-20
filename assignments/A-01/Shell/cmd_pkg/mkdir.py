import os
import sys

def makedir(command):
    file=command[1]
    if os.path.isdir(file):
        sys.stdout.write('Directory already exists')        
    else:
        os.makedirs(file)
        