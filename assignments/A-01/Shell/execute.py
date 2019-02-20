#!/usr/bin/env python
from cmd_pkg.commands import *
import sys
import threading
import multiprocessing 

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#execute command function takes function takes arguments like 
#command : which is to be performed
#history : once the command starts it is stored in history
#write : says how to write
 #write = 0 : writes on console
 #write = 1 : writes on a file with name write file
 #write = 2 : appends the result to write file
 
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
def executeCommand(command,history,write,writefile):
    cmd = command.split()
    background=0
    
    #if a command has & in it then the command is executed in the background
    if '&' in cmd:
        background=1
        # & is popped out 
        cmd.pop()
    
    #if the command has --help then it directly goes into the help istead of executing
    if '--help' in cmd:
        #initialises the thread and the function to be called is given in the target followed by arguments to thee function
        c= threading.Thread(target=helpfun,args=(cmd[0],write,writefile))
        if background==1 :
            #makes command to be run in the background
            c.daemon=True
            c.start()
        elif background==0:
            #makes thread start execution and wait till the command completes
            c.start()
            c.join()
    
    #if its not help then execute the command
    else:

        #cat command
        if(cmd[0]=='cat'):
            if write==0:
                c = threading.Thread(target=catfun,args=(cmd,))
                if background==1 :
                    c.daemon=True
                    c.start()
                elif background==0:
                    c.start()
                    c.join()
            else:
                c = threading.Thread(target=catfunwrite,args=(cmd,write,writefile))
                if background==1 :
                    c.daemon=True
                    c.start()
                elif background==0:
                    c.start()
                    c.join()
        
        #ls command
        if(cmd[0]=='ls'):
            if write==0:
                #if ls has flags then it calls the ls flag function
                if(len(cmd)>1):
                    c = threading.Thread(target=lsflag,args=(cmd,))
                    if background == 1:
                        c.daemon==True
                        c.start()
                    elif background==0:
                        c.start()
                        c.join()
                #just ls
                elif len(cmd)==1:
                    c = threading.Thread(target=lsfun)
                    if background == 1:
                        c.daemon==True
                        c.start()
                    elif background==0:
                        c.start()
                        c.join()
            #if the output is redirected to some file then call the following functions
            elif write > 0:
        
                if(len(cmd)>1):
                    c = threading.Thread(target=lsflagwrite,args=(cmd,write,writefile))
                    if background == 1:
                        c.daemon==True
                        c.start()
                    elif background==0:
                        c.start()
                        c.join()
                elif len(cmd)==1:
                    c = threading.Thread(target=lsfunwrite,args=(write,writefile))
                    if background == 1:
                        c.daemon==True
                        c.start()
                    elif background==0:
                        c.start()
                        c.join()
        #wc command
        if cmd[0]=='wc':
            if write==0 :
                c = threading.Thread(target=wcfun,args=(cmd,))
                if background == 1:
                    c.daemon==True
                    c.start()
                elif background==0:
                    c.start()
                    c.join()
            elif write>0:
                c = threading.Thread(target=wcfunwrite,args=(cmd,write,writefile))
                if background == 1:
                    c.daemon==True
                    c.start()
                elif background==0:
                    c.start()
                    c.join()

        #tail command
        if cmd[0]=='tail':
            if write==0 :
                if len(cmd) > 2:
                    if '-n' in cmd[1]:
                        filename=cmd[2]
                        countstr=str(cmd[1])
                        count=int(countstr[2:])
                    elif '-n' in cmd[2]:
                        filename = cmd[1]
                        countstr=str(cmd[2])
                        count=int(countstr[2:])
                    c=threading.Thread(target=tailfun2,args=(filename,count))
                elif len(cmd)==2:
                    c = threading.Thread(target=tailfun1,args=(cmd[1],))
                if background == 1:
                    c.daemon==True
                    c.start()
                elif background==0:
                    c.start()
                    c.join()
            elif write>0:
                
                if len(cmd) > 2:
                    if '-n' in cmd[1]:
                        filename=cmd[2]
                        countstr=str(cmd[1])
                        count=int(countstr[2:])
                    elif '-n' in cmd[2]:
                        filename = cmd[1]
                        countstr=str(cmd[2])
                        count=int(countstr[2:])
                    c=threading.Thread(target=tailfun2write,args=(filename,count,write,writefile))
                elif len(cmd)==2:
                    c = threading.Thread(target=tailfun1write,args=(cmd[1],write,writefile))
                if background == 1:
                    c.daemon==True
                    c.start()
                elif background==0:
                    c.start()
                    c.join()
    
        #head command
        if cmd[0]=='head':
            if write==0 :
                if len(cmd) > 2:
                    if '-n' in cmd[1]:
                        filename=cmd[2]
                        countstr=str(cmd[1])
                        count=int(countstr[2:])
                    elif '-n' in cmd[2]:
                        filename = cmd[1]
                        countstr=str(cmd[2])
                        count=int(countstr[2:])
                    c=threading.Thread(target=headfun2,args=(filename,count))
                elif len(cmd)==2:
                    c = threading.Thread(target=headfun1,args=(cmd[1],))
                if background == 1:
                    c.daemon==True
                    c.start()
                elif background==0:
                    c.start()
                    c.join()
            elif write>0:
                if len(cmd) > 2:
                    if '-n' in cmd[1]:
                        filename=cmd[2]
                        countstr=str(cmd[1])
                        count=int(countstr[2:])
                    elif '-n' in cmd[2]:
                        filename = cmd[1]
                        countstr=str(cmd[2])
                        count=int(countstr[2:])
                    c=threading.Thread(target=headfun2write,args=(filename,count,write,writefile))
                elif len(cmd)==2:
                    c = threading.Thread(target=headfun1write,args=(cmd[1],write,writefile))
                if background == 1:
                    c.daemon==True
                    c.start()
                elif background==0:
                    c.start()
                    c.join()
                
        #less function
        if(cmd[0]=='less' and background==0):
            if write==0 :
                c = threading.Thread(target=lessfun,args=(cmd,))
                if background == 1:
                    c.daemon==True
                    c.start()
                elif background==0:
                    c.start()
                    c.join()
            elif write>0:
                c = threading.Thread(target=lessfunwrite,args=(cmd,write,writefile))
                if background == 1:
                    c.daemon==True
                    c.start()
                elif background==0:
                    c.start()
                    c.join()

        #rm command
        if cmd[0]=='rm':
            c = threading.Thread(target=rmfun,args=(cmd,))
            if background == 1:
                c.daemon==True
                c.start()
            elif background==0:
                c.start()
                c.join()
        #rmdir command
        if cmd[0]=='rmdir':
            c = threading.Thread(target=removedir,args=(cmd,))
            if background == 1:
                c.daemon==True
                c.start()
            elif background==0:
                c.start()
                c.join()
    
        #mkdir function
        if cmd[0]=='mkdir':
            c = threading.Thread(target=makedir,args=(cmd,))
            if background == 1:
                c.daemon==True
                c.start()
            elif background==0:
                c.start()
                c.join()
    
        #cd function
        if cmd[0]=='cd':
            c = threading.Thread(target=cdfun,args=(cmd,))
            if background == 1:
                c.daemon==True
                c.start()
            elif background==0:
                c.start()
                c.join()
    
        #mv function
        if cmd[0]=='mv':
            c = threading.Thread(target=mvfun,args=(cmd,))
            if background == 1:
                c.daemon==True
                c.start()
            elif background==0:
                c.start()
                c.join()

        #cp function
        if cmd[0]=='cp':
            c = threading.Thread(target=cpfun,args=(cmd,))
            if background == 1:
                c.daemon==True
                c.start()
            elif background==0:
                c.start()
                c.join()
    
    
        #pwd function
        if cmd[0]=='pwd':
            if write==0 :
                c = threading.Thread(target=pwdfun)
                if background == 1:
                    c.daemon==True
                    c.start()
                elif background==0:
                    c.start()
                    c.join()
            elif write>0:
                c = threading.Thread(target=pwdwrite,args=(write,writefile))
                if background == 1:
                    c.daemon==True
                    c.start()
                elif background==0:
                    c.start()
                    c.join()
    
        #grep function
        if cmd[0]=='grep':
            if write==0 :
                c = threading.Thread(target=grepfun,args=(cmd,))
                if background == 1:
                    c.daemon==True
                    c.start()
                elif background==0:
                    c.start()
                    c.join()
            elif write>0:
                c = threading.Thread(target=grepfunwrite,args=(cmd,write,writefile))
                if background == 1:
                    c.daemon==True
                    c.start()
                elif background==0:
                    c.start()
                    c.join()
    

        #history
        if cmd[0]=='history':
            if write==0 :
                c = threading.Thread(target=historyfun,args=(cmd,history))
                if background == 1:
                    c.daemon==True
                    c.start()
                elif background==0:
                    c.start()
                    c.join()
            elif write>0:
                c = threading.Thread(target=historyfunwrite,args=(cmd,history,write,writefile))
                if background == 1:
                    c.daemon==True
                    c.start()
                elif background==0:
                    c.start()
                    c.join()

        #sort
        if cmd[0]=='sort':
            if write==0 :
                c = threading.Thread(target=sortfun,args=(cmd[1],))
                if background == 1:
                    c.daemon==True
                    c.start()
                elif background==0:
                    c.start()
                    c.join()
            elif write>0:
                c = threading.Thread(target=sortfunwrite,args=(cmd[1],write,writefile))
                if background == 1:
                    c.daemon==True
                    c.start()
                elif background==0:
                    c.start()
                    c.join()

        #who
        if cmd[0]=='who':
            if write==0 :
                c = threading.Thread(target=whofun)
                if background == 1:
                    c.daemon==True
                    c.start()
                elif background==0:
                    c.start()
                    c.join()
            elif write>0:
                c = threading.Thread(target=whofunwrite,args=(write,writefile))
                if background == 1:
                    c.daemon==True
                    c.start()
                elif background==0:
                    c.start()
                    c.join()
    
        #chmod
        if cmd[0]=='chmod':
            chmodfun(cmd)
        
        #exit
        if(cmd[0]=='exit' ):
            sys.exit()

#main function
if __name__ == '__main__':
    #let rawcmd be list which store the commnds history
    rawcmd=[]
    temphistory=[]
    #the commands implemented in the shell are taken into args
    args=('cat','cd','chmod','cp','exit','grep','head','history','less','ls','mkdir','mv','pwd','rm','rmdir','who','wc','tail','sort')
    #run till true
    while True:
        
        #have a % symbol during the input
        cmd = input('% ')
        rawcmd.append(cmd)
        
        if '!' in cmd:
            number=int(cmd[1])
            if number < len(rawcmd):
                cmd=rawcmd[number]
            else:
                print('History not available for that number')

        checkarg = cmd.split()
        
        if 'exit' in cmd:
            sys.exit() 
        
        specialchar=('<','>','>>','|')
        tempfile="output.txt"
        if '>' in cmd or '>>' in cmd:
            if '>>' in cmd:
                tempcommand=cmd.split('>>')
                appendfile=tempcommand[1]
                if '|' in cmd:
                    tempgrepcommands = tempcommand[0]
                    grepcommands = tempgrepcommands.split('|')
                    first=0
                    for i in grepcommands:
                        i=i.strip()
                        first+=1
                        if first == 1:
                            executeCommand(i,rawcmd,1,"output.txt")
                            i=" "
                        else:
                            i+=" "
                            i+=tempfile
                            executeCommand(i,rawcmd,1,"output.txt")
                            i=" "
                    printstr=""
                    with open("output.txt",'r') as r:
                        lines=r.readlines()
                        for line in lines:
                            printstr+=line
                    with open(appendfile,'w') as f:
                        f.write(str(printstr))
                else:
                    executeCommand(tempcommand[0],rawcmd,2,tempcommand[1])

            elif '>' in cmd:
                tempcommand1=cmd.split('>')
                writefile=tempcommand1[1]
                if '|' in cmd:
                    tempgrepcommands1 = tempcommand1[0]
                    grepcommands1 = tempgrepcommands1.split('|')
                    first=0
                    for i in grepcommands1:
                        i=i.strip()
                        first+=1
                        if first == 1:
                            executeCommand(i,rawcmd,1,"output.txt")
                            i=" "
                        else:
                            i+=" "
                            i+=tempfile
                            executeCommand(i,rawcmd,1,"output.txt")
                            i=" "
                    printstr=""
                    with open("output.txt",'r') as r:
                        lines=r.readlines()
                        for line in lines:
                            printstr+=line
                    with open(writefile,'w') as f:
                        f.write(str(printstr))
                else:
                    executeCommand(tempcommand1[0],rawcmd,1,tempcommand1[1])
        elif '|' in cmd:
            grepcomm = cmd.split('|')
            commlength=len(grepcomm)
            firstcommand=grepcomm[0]
            lastcommand=grepcomm[commlength-1]
            for i in grepcomm:
                if i == firstcommand:
                    i=i.strip()
                    executeCommand(i,rawcmd,1,"output.txt")
                elif i== lastcommand:
                    i+=" "
                    i+="output.txt"
                    executeCommand(i,rawcmd,0,"output.txt")
                else:
                    i+=" "
                    i+="output.txt"
                    executeCommand(i,rawcmd,1,"output.txt")        
        elif checkarg[0] in args:
            executeCommand(cmd,rawcmd,0,cmd)
        
        else:
            print(checkarg[0],'command not found')