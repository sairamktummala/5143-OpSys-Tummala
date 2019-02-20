import os 
import sys
import shutil
import pathlib
import fnmatch
path=os.getcwd()
def rmfun(command):
    commandlength=len(command)
    if commandlength < 3 :
        param=command[1]
        if '*' not in param:
            removeFile(param)
        elif ('*' in param):
            removeSpecificFiles(param)
    else:
        if '-rf' in command:
            removeAllFilesInDirectory(command[2])
    
    
def removeAllFilesInDirectory(file):
    if os.path.isdir(file):
        shutil.rmtree(file)
    else:
        sys.stdout.write('rm: cannot remove ')
        sys.stdout.write(file)
        sys.stdout.write(':does not exist')
        sys.stdout.write('\n')
        
def removeSpecificFiles(param):
    Filesindirectory=os.listdir('.')
    count = 0
    for file in Filesindirectory:
        if fnmatch.fnmatch(file,param):
            if os.path.isfile(file):
                count+=1
                os.remove(file)
            elif os.path.isdir(file):
                sys.stdout.write('rm: cannot remove ')
                sys.stdout.write(file)
                sys.stdout.write(':is a directory')
                sys.stdout.write('\n')
            else:
                sys.stdout.write('rm: cannot remove ')
                sys.stdout.write(param)
                sys.stdout.write(': No such file or directory')
                sys.stdout.write('\n')
     

    
def removeFile(file): 
    
    if os.path.isfile(file):
        os.remove(file)
    elif os.path.isdir(file):
        sys.stdout.write('cannot delete directory')
        sys.stdout.write('\n')

    else:
        sys.stdout.write('file not found')
        sys.stdout.write('\n')
    
