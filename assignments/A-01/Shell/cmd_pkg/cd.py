import os
import sys
def cdfun(command):
    #pass to a fucntion according to flags
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
        
#if flag is ~
def cdfun1():
    os.chdir(os.path.expanduser("~"))

#if flag is ..
def cdfun2():
    os.chdir("..")

#if a path is specified to change
def cdfun3(path):
    os.chdir(path)
    