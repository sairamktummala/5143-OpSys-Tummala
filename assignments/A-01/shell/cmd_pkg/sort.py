import os 
import sys
def sortfun(file):
    strsort=""
    if os.path.exists(file):
        with open(file) as fvar:
            lines=fvar.readlines()
            lines.sort()
            for i in lines:
                strsort+=i
        fil=open(file,'w')
        fil.write(strsort)
        

    else:
        sys.stdout.write('file not found')
        sys.stdout.write('\n')
    return strsort

#write
def sortfunwrite(file,write,writefile):
    strsort=""
    if os.path.exists(file):
        with open(file) as fvar:
            lines=fvar.readlines()
            lines.sort()
            for i in lines:
                strsort+=i
        
        writefile=writefile.strip()
        if(write==1):
            with open(writefile, 'w') as f:
                f.write(strsort)
        elif(write==2):
            with open(writefile,'a') as f:
                f.write(strsort)
        elif(write==3):
            return strsort
        

    else:
        sys.stdout.write('file not found')
        sys.stdout.write('\n')
    return strsort