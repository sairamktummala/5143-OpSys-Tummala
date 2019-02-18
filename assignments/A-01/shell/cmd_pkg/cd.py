import os
import sys
def cdfun(command):
    if len(command)>1:
        exp=command[1]
        if(exp ==".."):
            cdfun2()
        elif(exp=="~"):
            cdfun1()
        else:
            cdfun3(command[1])
    else:
        cdfun1()
        

def cdfun1():
    os.chdir(os.path.expanduser("~"))
def cdfun2():
    os.chdir("..")
def cdfun3(path):
    os.chdir(path)
    