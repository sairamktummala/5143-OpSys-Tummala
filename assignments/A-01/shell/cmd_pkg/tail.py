import sys
def tailfun(command):
    if len(command)>2 :
        tailfun2(command[2],command[1])
    else:
        tailfun1(command[1])


def tailfun1(file):
    linelist = []
    with open(file) as fvar:
        lineCount=0
        for lines in fvar:
            linelist.append(lines)
            lineCount += 1
    tempCOunt = int(lineCount) - 10
    linelist = linelist[tempCOunt:]
    for l in linelist:
        sys.stdout.write(l)
    sys.stdout.write('\n')

def tailfun2(file,count):
    linelist = []
    with open(file) as fvar:
        lineCount=0
        for lines in fvar:
            linelist.append(lines)
            lineCount += 1
    tempCOunt = int(lineCount) - int(count)
    linelist = linelist[int(tempCOunt):]
    for l in linelist:
        sys.stdout.write(l)
    sys.stdout.write('\n')
  

  #write functions
def tailfunwrite(command,write,writefile):
    if len(command)>2 :
        tailfun2write(command[2],command[1],write,writefile)
    else:
        tailfun1write(command[1],write,writefile)


def tailfun1write(file,write,writefile):
    linelist = []
    returnstr=""
    with open(file) as fvar:
        lineCount=0
        for lines in fvar:
            linelist.append(lines)
            lineCount += 1
    tempCOunt = int(lineCount) - 10
    linelist = linelist[tempCOunt:]
    for l in linelist:
        returnstr+=l
    returnstr+='\n'
    
    writefile=writefile.strip()
    if(write==1):
        with open(writefile, 'w') as f:
            f.write(returnstr)
    elif(write==2):
        with open(writefile,'a') as f:
            f.write(returnstr)
    elif(write==3):
        return returnstr

def tailfun2write(file,count,write,writefile):
    returnstr=""
    linelist = []
    with open(file) as fvar:
        lineCount=0
        for lines in fvar:
            linelist.append(lines)
            lineCount += 1
    tempCOunt = int(lineCount) - int(count)
    linelist = linelist[int(tempCOunt):]
    for l in linelist:
        returnstr+=l
    returnstr+='\n'
        
    writefile=writefile.strip()
    if(write==1):
        with open(writefile, 'w') as f:
            f.write(returnstr)
    elif(write==2):
        with open(writefile,'a') as f:
            f.write(returnstr)
    elif(write==3):
        return returnstr