import os
import sys
def chmodfun(cmd):
    filename = cmd[2]
    str=int(cmd[1])
    if os.path.isfile(filename):
        os.chmod(filename,str)
    else:
        sys.stdout.write('file not found')