import os
import sys

path = os.getcwd()
def catfun(cmd):
    content=''
    for i in range(1,len(cmd)):
        if os.path.isfile(cmd[i]):
            data=open(cmd[i])
            content+=(data.read())
        else:
            sys.stdout.write('\033[1;31;40m ')
            sys.stdout.write(cmd[i])
            sys.stdout.write(':No such File exist\033[1;m')
            sys.stdout.write('\n')
        sys.stdout.write(content)
        sys.stdout.write('\n')
def catfunwrite(cmd,write,writefile):
    content=''
    for i in range(1,len(cmd)):
        if os.path.isfile(cmd[i]):
            data=open(cmd[i])
            content+=(data.read())
        else:
            sys.stdout.write('\033[1;31;40m ')
            sys.stdout.write(cmd[i])
            sys.stdout.write(':No such File exist\033[1;m')
            sys.stdout.write('\n')
    writefile = writefile.strip()
    if(write==1):
        with open(writefile, 'w') as f:
            f.write(content)
    elif(write==2):
        with open(writefile,'a') as f:
            f.write(content)
    elif(write==3):
        return content
