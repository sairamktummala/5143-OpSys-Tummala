import os
import getpass
import sys
def whofun():
    sys.stdout.write(getpass.getuser())

#write
def whofunwrite(write,writefile):
    returnstri = ""
    returnstri+= getpass.getuser()
    
    writefile=writefile.strip()
    if(write==1):
        with open(writefile, 'w') as f:
            f.write(returnstri)
    elif(write==2):
        with open(writefile,'a') as f:
            f.write(returnstri)
    elif(write==3):
        return returnstri