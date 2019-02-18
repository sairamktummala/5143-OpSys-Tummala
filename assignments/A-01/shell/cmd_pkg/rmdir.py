import os
import sys
import shutil
def removedir(command):
    file=command[1]
    if os.path.exists(file):
        shutil.rmtree(file)
    else:
        sys.stdout.write(file)
        sys.stdout.write(': No such directory exists')
        sys.stdout.write('\n')