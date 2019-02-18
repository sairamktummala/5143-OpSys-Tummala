import os 
import sys
import shutil
import pathlib
import fnmatch
path=os.getcwd()
def rmfun(command):
    param=command[1]
    if '*' not in param:
        removeFile(param)
    elif ('*' in param):
        removeSpecificFiles(param)
    elif(param == 'r*' ):
        removeAllFilesInDirectory()
    
    
def removeAllFilesInDirectory():
    currentDirectory=pathlib.Path('.')
    shutil.rmtree(currentDirectory)
        
def removeSpecificFiles(param):
    Filesindirectory=os.listdir('.')
    count = 0
    for file in Filesindirectory:
        if fnmatch.fnmatch(file,param):
            if os.path.isfile(file):
                count+=1
                os.remove(file)
            else:
                sys.stdout.write('rm: cannot remove ')
                sys.stdout.write(param)
                sys.stdout.write(': No such file or directory')
                sys.stdout.write('\n')

    
def removeFile(file):   
    if os.path.exists(file):
        os.remove(file)
    else:
        sys.stdout.write('file not found')
        sys.stdout.write('\n')
    
