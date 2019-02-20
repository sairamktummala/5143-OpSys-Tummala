import sys

def historyfun(cmd,history):
    
    stringhistory=""
    for i in history:
        stringhistory+=i
        stringhistory+="\n"

    sys.stdout.write(stringhistory)


#write
def historyfunwrite(cmd,history,write,writefile):
    stringhistory=""
    for i in history:
        stringhistory+=i
    writefile=writefile.strip()
    if(write==1):
        with open(writefile, 'w') as f:
            f.write(stringhistory)
    elif(write==2):
        with open(writefile,'a') as f:
            f.write(stringhistory)
    elif(write==3):
        return stringhistory