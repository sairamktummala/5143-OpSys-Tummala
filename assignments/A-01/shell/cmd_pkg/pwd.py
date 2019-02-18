import sys
import os
def pwdfun():
    returnString=os.getcwd()
    sys.stdout.write(returnString)
    sys.stdout.write('\n')
def pwdwrite(write,writefile):
    returnString=os.getcwd()
    writefile=writefile.strip()
    if(write==1):
        with open(writefile, 'w') as f:
            f.write(returnString)
    elif(write==2):
        with open(writefile,'a') as f:
            f.write(returnString)
    elif(write==3):
        return returnString
    
