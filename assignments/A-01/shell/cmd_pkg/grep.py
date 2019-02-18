import sys
import os
import re

def grepfun(args):
    if(args[1]=='-l'):
        pattern=args[2]
        grepListing(pattern)
    else:
        pattern=args[1]
        stri =""
        for i in args[2:]:
            stri+=grepcheckfile(i,pattern)
        sys.stdout.write(stri)
def grepListing(pattern):
    path=os.listdir('.')
    strinf=""
    a=set()
    for file in path:
        if os.path.isfile(file):
            with open(file) as fvar:
                for lines in fvar:
                    line = re.findall(pattern,lines)
                    if not line:
                        pass 
                    else:
                        tempstring = file
                        a.add(tempstring)
        else:
            pass
    returnstri=""
    for i in a:
        returnstri+=i
        returnstri+='\n'
    sys.stdout.write(returnstri)


def grepcheckfile(file,pattern):
    if os.path.isfile(file):
        strin2 = grepGetThelist(file,pattern)
        return strin2
    elif os.path.exists(file):
        strngh = " "
        return strngh
    else:
        sys.stdout.write(file)
        sys.stdout.write('\033[1;31;40m  :No such File exist\033[1;m')
        sys.stdout.write('\n')
        strngh = " "
        return strngh
    
def grepGetThelist(file,pattern):
    strin=""
    with open(file) as fvar:
        lineCount = 0
        for lines in fvar:
            line = re.findall(pattern, lines)
            if not line:
                pass
            else:
                tempstring = file + ":" + str(lines)
                strin+=tempstring
    strin+=('\n')
    return strin


#write starts here
def grepfunwrite(args,write,writefile):
    if(args[1]=='-l'):
        pattern=args[2]
        grepListingwrite(pattern,write,writefile)
    else:
        pattern=args[1]
        stri =""
        for i in args[2:]:
            stri+=grepcheckfilewrite(i,pattern)

        writefile=writefile.strip()
        if(write==1):
            with open(writefile, 'w') as f:
                f.write(stri)
        elif(write==2):
            with open(writefile,'a') as f:
                f.write(stri)
        elif(write==3):
            return stri



def grepListingwrite(pattern,write,writefile):
    path=os.listdir('.')
    strinf=""
    a=set()
    for file in path:
        if os.path.isfile(file):
            with open(file) as fvar:
                for lines in fvar:
                    line = re.findall(pattern,lines)
                    if not line:
                        pass 
                    else:
                        tempstring = file
                        a.add(tempstring)
        else:
            pass
    returnstri=""
    for i in a:
        returnstri+=i
        returnstri+='\n'
    
    writefile=writefile.strip()
    if(write==1):
        with open(writefile, 'w') as f:
            f.write(returnstri)
    elif(write==2):
        with open(writefile,'a') as f:
            f.write(returnstri)
    elif(write==3):
        return returnstri


def grepcheckfilewrite(file,pattern):
    if os.path.isfile(file):
        strin2 = grepGetThelistwrite(file,pattern)
        return strin2
    elif os.path.exists(file):
        strngh = " "
        return strngh
    else:
        sys.stdout.write(file)
        sys.stdout.write('\033[1;31;40m  :No such File exist\033[1;m')
        sys.stdout.write('\n')
        strngh = " "
        return strngh
    
def grepGetThelistwrite(file,pattern):
    strin=""
    with open(file) as fvar:
        lineCount = 0
        for lines in fvar:
            line = re.findall(pattern, lines)
            if not line:
                pass
            else:
                tempstring = file + ":" + str(lines)
                strin+=tempstring
    strin+=('\n')
    return strin