import os
import sys
def chmodfun(cmd):
    filename = cmd[2]
    if os.path.isfile(filename):
        os.chmod(filename,int(cmd[1],8))
    elif os.path.isdir(filename):
        os.chmod(filename,int(cmd[1],8))
    else:
        sys.stdout.write('file not found')