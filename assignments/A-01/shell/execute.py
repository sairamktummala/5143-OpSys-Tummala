#!/usr/bin/env python
from cmd_pkg.commands import *
import sys
import threading
import multiprocessing 
  
def executeCommand(command,history,write,writefile):
    history+=command
    history+=('\n')
    cmd = command.split()
    background=0
    if '&' in cmd:
        background=1
        cmd.pop()
    if '--help' in cmd:
        c= threading.Thread(target=helpfun,args=(cmd[0],write,writefile))
        if background==1 :
            c.daemon=True
            c.start()
        elif background==0:
            c.start()
            c.join()
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
                if(len(cmd)>1):
                    c = threading.Thread(target=lsflag,args=(cmd,))
                    if background == 1:
                        c.daemon==True
                        c.start()
                    elif background==0:
                        c.start()
                        c.join()
                elif len(cmd)==1:
                    c = threading.Thread(target=lsfun)
                    if background == 1:
                        c.daemon==True
                        c.start()
                    elif background==0:
                        c.start()
                        c.join()
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
                c = threading.Thread(target=tailfun,args=(cmd,))
                if background == 1:
                    c.daemon==True
                    c.start()
                elif background==0:
                    c.start()
                    c.join()
            elif write>0:
                c= threading.Thread(target=tailfunwrite,args=(cmd,write,writefile))
                if background == 1:
                    c.daemon==True
                    c.start()
                elif background==0:
                    c.start()
                    c.join()
    
        #head command
        if cmd[0]=='head':
            if write==0 :
                c = threading.Thread(target=headfun,args=(cmd,))
                if background == 1:
                    c.daemon==True
                    c.start()
                elif background==0:
                    c.start()
                    c.join()
            elif write>0:
                c = threading.Thread(target=headfunwrite,args=(cmd,write,writefile))
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

if __name__ == '__main__':
    history=[]
    args=('cat','cd','chmod','cp','exit','grep','head','history','less','ls','mkdir','mv','pwd','rm','rmdir','who','wc','tail','sort')
    while True:
        cmd = input('% ')
        checkcmd = cmd.split()
        ccommand=checkcmd[0]
        if ccommand in args:
            if '|' in cmd :
                write=1
                commandlist=cmd.split('|')
                last = len(commandlist)-1
                command1 = commandlist[0].strip()
                tempfile='result.txt'
                executeCommand(command1,history,1,tempfile)
                first = 1
                while first < last :
                    commandtemp=commandlist[first].strip()
                    tempcheck=commandtemp.split()
                    if tempcheck[0] in args:
                        commandtemp+=' '
                        commandtemp+=tempfile
                        executeCommand(commandtemp,history,1,tempfile)
                        first+=1
                    else:
                        print('bash: ',commandtemp,': command not found')
                commandlast = commandlist[last].strip()
                temcom=commandlast.split()
                if temcom[0] in args:
                    commandlast+=' '
                    commandlast+=tempfile
                    executeCommand(commandlast,history,0,cmd)
                else:
                    print('bash: ',commandlast,': command not found')
            else:
                write=0
                command=""
                if '>>' in cmd:
                    cmd=cmd.split('>>')
                    write=2
                    command=cmd[0]
                    file=cmd[1]
                    executeCommand(command,history,write,file)
                elif '>' in cmd:
                    write=1
                    cmd=cmd.split('>')
                    command=cmd[0]
                    file=cmd[1]
                    executeCommand(command,history,write,file)
                elif '<' in cmd:
                    tempcommandlist = cmd.split('<')
                    tempcommand = tempcommandlist[0]
                    tempfilename = tempcommandlist[1].strip()
                    finalcommand = tempcommand + tempfilename
                    executeCommand(finalcommand,history,0,cmd)
                else :
                    executeCommand(cmd,history,write,cmd)
        else:
            
            print('bash: ',ccommand,': command not found')
        