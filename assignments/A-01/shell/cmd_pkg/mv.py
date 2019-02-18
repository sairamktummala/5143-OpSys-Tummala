import shutil
import os
import sys
path=os.getcwd()
def mvfun(command):
    file1=command[1]
    file2=command[2]
    if os.path.isdir(file1):
        if os.path.isdir(file2):
            sys.stdout.write(file2)
            sys.stdout.write('\033[1;31;40m :Already exist\033[1;m')
            sys.stdout.write('\n') 
        else:
            shutil.move(file1,file2)
    else:
        sys.stdout.write(file1)
        sys.stdout.write('\033[1;31;40m :Desnot exist\033[1;m')