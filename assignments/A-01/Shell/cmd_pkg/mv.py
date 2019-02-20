import shutil
import os
import sys
path=os.getcwd()
def mvfun(command):
    file1=command[1]
    file2=command[2]
    if os.path.isfile(file1):
        shutil.move(file1,file2)
    elif os.path.isdir(file2):
        shutil.move(file1,file2)
    else:
        print(file1,"No such file exists")
