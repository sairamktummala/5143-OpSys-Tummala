import os
import sys
import stat
import time
from os import listdir
from stat import *
import time,subprocess,shutil

def lsfun():
    filename=os.listdir('.')
    for name in filename:
            if(name.startswith('.')):
                    pass
            else:
                    sys.stdout.write(name)
                    sys.stdout.write('\n')

def lsflag(cmd):
        note = 0
        temp=" "
        if len(cmd) == 2:
                note = 0
                if(cmd[1]=='-l'):
                        lslfun(note,temp)
                elif(cmd[1]=='-a'):
                        lsafun(note,temp)
                elif(cmd[1]=='-h'):
                        lshfun(note,temp)
                elif(cmd[1]=='-lah'):
                        lslahfun(note,temp)
                elif(os.path.isdir(cmd[1])):
                        lsfile(cmd[1])
                else:
                        sys.stdout.write('flagnot found')
        elif len(cmd) == 3:
                count=0
                note=1
                for i in cmd:
                        if '-' in i:
                                break
                        else:
                                count+=1
                if count == 1:
                        filename = cmd[2]
                        flag = cmd[1] 
                elif count == 2:
                        filename = cmd[1]
                        flag =cmd[2]
                if flag == "-l":
                        lslfun(note,filename)
                elif flag == "-a":
                        lsafun(note,filename)
                elif flag == "-h":
                        lshfun(note,filename)
                elif flag == "-lah":
                        lshfun(note,filename)
                else:
                        sys.stdout.write("invalid flag")
        
def lsfile(dir):
        filename=os.listdir('.')
        for name in filename:
                if(name.startswith('.')):
                        pass
                else:
                        sys.stdout.write(name)
                        sys.stdout.write('\n')


def lsafun(note,dir):
        if note == 0 :
                dir=os.listdir('.')
                for name in dir:
                        sys.stdout.write(name)
                        sys.stdout.write('\n')
        elif note == 1:
                dir=os.listdir(dir)
                for name in dir:
                        sys.stdout.write(name)
                        sys.stdout.write('\n')
def lslfun(note,dir):
        
        if note == 1:
                files=os.listdir(dir)
                for file in files:
                        if file.startswith('.'):
                                pass
                        else:
                                printablestr=""
                                mode=os.lstat(file).st_mode
                                if S_ISDIR(mode):
                                        perm='d'
                                else:
                                        perm='-'
                                s = str(oct(os.stat(file)[stat.ST_MODE])[-3:])
                                permission={'0' :'---', '1' : '--x', '2' : '-w-','3' : '-wx','4':'r--','5':'r-x','6':'rw-','7':'rwx'}
                                userperm=permission[s[0]]
                                groupperm=permission[s[1]]
                                otherperm=permission[s[2]]
                                permstring=perm+userperm+groupperm+otherperm
                                printablestr+=permstring
                                stlin=str(os.stat(file)[stat.ST_NLINK])
                                printablestr+=stlin
                                printablestr+='\t'
                                size= str(os.stat(file).st_size)
                                printablestr+=size
                                printablestr+='\t'
                                modifiedTime=str(time.ctime(os.path.getmtime(file)))
                                printablestr+=modifiedTime
                                printablestr+='\t'
                                printablestr+=file
                                sys.stdout.write(printablestr)
                                sys.stdout.write('\n')

        
        
        elif(note==0):
                path=os.getcwd()
                files=os.listdir(path)
                for file in files:
                        if file.startswith('.'):
                                pass
                        else:
                                printablestr=""
                                mode=os.stat(file).st_mode
                                if S_ISDIR(mode):
                                        perm='d'
                                else:
                                        perm='-'
                                s = str(oct(os.stat(file)[stat.ST_MODE])[-3:])
                                permission={'0' :'---', '1' : '--x', '2' : '-w-','3' : '-wx','4':'r--','5':'r-x','6':'rw-','7':'rwx'}
                                userperm=permission[s[0]]
                                groupperm=permission[s[1]]
                                otherperm=permission[s[2]]
                                permstring=perm+userperm+groupperm+otherperm
                                printablestr+=permstring
                                stlin=str(os.stat(file)[stat.ST_NLINK])
                                printablestr+=stlin
                                printablestr+='\t'
                                size= str(os.stat(file).st_size)
                                printablestr+=size
                                printablestr+='\t'
                                modifiedTime=str(time.ctime(os.path.getmtime(file)))
                                printablestr+=modifiedTime
                                printablestr+='\t'
                                printablestr+=file
                                sys.stdout.write(printablestr)
                                sys.stdout.write('\n')
def lshfun(note,dir):
        
        if(note == 1):
                files=os.listdir(dir)
                for file in files:
                        if file.startswith('.'):
                                pass
                        else:
                                printablestr=""
                                mode=os.stat(file).st_mode
                                if S_ISDIR(mode):
                                        perm='d'
                                else:
                                        perm='-'
                                s = str(oct(os.stat(file)[stat.ST_MODE])[-3:])
                                permission={'0' :'---', '1' : '--x', '2' : '-w-','3' : '-wx','4':'r--','5':'r-x','6':'rw-','7':'rwx'}
                                userperm=permission[s[0]]
                                groupperm=permission[s[1]]
                                otherperm=permission[s[2]]
                                permstring=perm+userperm+groupperm+otherperm
                                printablestr+=permstring
                                stlin=str(os.stat(file)[stat.ST_NLINK])
                                printablestr+=stlin
                                printablestr+='\t'
                                size= str(os.stat(file).st_size)
                                psize='0'
                                if int(size)<1024:
                                        psize=size+'B'
                                elif int(size)<1048576:
                                        psize=size[0]+'.'+size[1]+'K'
                                elif int(size)>1048576:
                                        psize=size[0]+'.'+size[1]+'GB'
                                printablestr+=psize
                                printablestr+='\t'
                                modifiedTime=str(time.ctime(os.path.getmtime(file)))
                                printablestr+=modifiedTime
                                printablestr+='\t'
                                printablestr+=file
                                sys.stdout.write(printablestr)
                                sys.stdout.write('\n')
        elif(note==0):
                path=os.getcwd()
                files=os.listdir(path)
                for file in files:
                        if file.startswith('.'):
                                pass
                        else:
                                printablestr=""
                                mode=os.stat(file).st_mode
                                if S_ISDIR(mode):
                                        perm='d'
                                else:
                                        perm='-'
                                s = str(oct(os.stat(file)[stat.ST_MODE])[-3:])
                                permission={'0' :'---', '1' : '--x', '2' : '-w-','3' : '-wx','4':'r--','5':'r-x','6':'rw-','7':'rwx'}
                                userperm=permission[s[0]]
                                groupperm=permission[s[1]]
                                otherperm=permission[s[2]]
                                permstring=perm+userperm+groupperm+otherperm
                                printablestr+=permstring
                                stlin=str(os.stat(file)[stat.ST_NLINK])
                                printablestr+=stlin
                                printablestr+='\t'
                                size= str(os.stat(file).st_size)
                                psize='0'
                                if int(size)<1024:
                                        psize=size+'B'
                                elif int(size)<1048576:
                                        psize=size[0]+'.'+size[1]+'K'
                                elif int(size)>1048576:
                                        psize=size[0]+'.'+size[1]+'GB'
                                printablestr+=psize
                                printablestr+='\t'
                                modifiedTime=str(time.ctime(os.path.getmtime(file)))
                                printablestr+=modifiedTime
                                printablestr+='\t'
                                printablestr+=file
                                sys.stdout.write(printablestr)
                                sys.stdout.write('\n')
       
def lslahfun(note,dir):
        path=os.getcwd()
        files=os.listdir(path)
        for file in files:
                printablestr=""
                mode=os.stat(file).st_mode
                if S_ISDIR(mode):
                        perm='d'
                else:
                        perm='-'
                s = str(oct(os.stat(file)[stat.ST_MODE])[-3:])
                permission={'0' :'---', '1' : '--x', '2' : '-w-','3' : '-wx','4':'r--','5':'r-x','6':'rw-','7':'rwx'}
                userperm=permission[s[0]]
                groupperm=permission[s[1]]
                otherperm=permission[s[2]]
                permstring=perm+userperm+groupperm+otherperm
                printablestr+=permstring
                stlin=str(os.stat(file)[stat.ST_NLINK])
                printablestr+=stlin
                printablestr+='\t'
                size= str(os.stat(file).st_size)
                psize='0'
                if int(size)<1024:
                        psize=size+'B'
                elif int(size)<1048576:
                        psize=size[0]+'.'+size[1]+'K'
                elif int(size)>1048576:
                        psize=size[0]+'.'+size[1]+'GB'
                printablestr+=psize
                printablestr+='\t'
                modifiedTime=str(time.ctime(os.path.getmtime(file)))
                printablestr+=modifiedTime
                printablestr+='\t'
                printablestr+=file
                sys.stdout.write(printablestr)
                sys.stdout.write('\n')
                

#write starts here
def lsfunwrite(write,wfile):
        filename=os.listdir('.')
        tempstr=''
        for name in filename:
                if(name.startswith('.')):
                        pass
                else:
                        tempstr+=name
                        tempstr+='\n'
        if(write==1):
                with open(wfile, 'w') as f:
                        f.write(tempstr)
        elif(write==2):
                with open(wfile,'a') as f:
                        f.write(tempstr)
        elif(write==3):
                return tempstr

def lsflagwrite(cmd,write,wfile):
        if(cmd[1]=='-l'):
                lslfunwrite(write,wfile)
        elif(cmd[1]=='-a'):
                lsafunwrite(write,wfile)
        elif(cmd[1]=='-h'):
                lshfunwrite(write,wfile)

def lsafunwrite(write,wfile):
    dir=os.listdir('.')
    printstr=""
    for name in dir:
            printstr+=name
            printstr+='\n'
    wfile = wfile.strip()
    if(write==1):
            with open(wfile, 'w') as f:
                    f.write(printstr)
    elif(write==2):
            with open(wfile,'a') as f:
                    f.write(printstr)
    elif(write==3):
            return tempstr
 
def lslfunwrite(write,wfile):
        path=os.getcwd()
        finalprintstr=""
        files=os.listdir(path)
        for file in files:
                if file.startswith('.'):
                        pass
                else:
                        printablestr=""
                        mode=os.stat(file).st_mode
                        if S_ISDIR(mode):
                                perm='d'
                        else:
                                perm='-'
                        s = str(oct(os.stat(file)[stat.ST_MODE])[-3:])
                        permission={'0' :'---', '1' : '--x', '2' : '-w-','3' : '-wx','4':'r--','5':'r-x','6':'rw-','7':'rwx'}
                        userperm=permission[s[0]]
                        groupperm=permission[s[1]]
                        otherperm=permission[s[2]]
                        permstring=perm+userperm+groupperm+otherperm
                        printablestr+=permstring
                        stlin=str(os.stat(file)[stat.ST_NLINK])
                        printablestr+=stlin
                        printablestr+='\t'
                        size= str(os.stat(file).st_size)
                        printablestr+=size
                        printablestr+='\t'
                        modifiedTime=str(time.ctime(os.path.getmtime(file)))
                        printablestr+=modifiedTime
                        printablestr+='\t'
                        printablestr+=file
                        finalprintstr+=printablestr
                        finalprintstr+='\n'   
        wfile = wfile.strip()
        if(write==1):
                with open(wfile, 'w') as f:
                        f.write(finalprintstr)
        elif(write==2):
                with open(wfile,'a') as f:
                        f.write(finalprintstr)
        elif(write==3):
                return finalprintstr
def lshfunwrite(write,wfile):
        path=os.getcwd()
        files=os.listdir(path)
        finalprintstr=""
        for file in files:
                if file.startswith('.'):
                        pass
                else:
                        printablestr=""
                        mode=os.stat(file).st_mode
                        if S_ISDIR(mode):
                                perm='d'
                        else:
                                perm='-'
                        s = str(oct(os.stat(file)[stat.ST_MODE])[-3:])
                        permission={'0' :'---', '1' : '--x', '2' : '-w-','3' : '-wx','4':'r--','5':'r-x','6':'rw-','7':'rwx'}
                        userperm=permission[s[0]]
                        groupperm=permission[s[1]]
                        otherperm=permission[s[2]]
                        permstring=perm+userperm+groupperm+otherperm
                        printablestr+=permstring
                        stlin=str(os.stat(file)[stat.ST_NLINK])
                        printablestr+=stlin
                        printablestr+='\t'
                        size= str(os.stat(file).st_size)
                        psize='0'
                        if int(size)<1024:
                                psize=size+'B'
                        elif int(size)<1048576:
                                psize=size[0]+'.'+size[1]+'K'
                        elif int(size)>1048576:
                                psize=size[0]+'.'+size[1]+'GB'
                        printablestr+=psize
                        printablestr+='\t'
                        modifiedTime=str(time.ctime(os.path.getmtime(file)))
                        printablestr+=modifiedTime
                        printablestr+='\t'
                        printablestr+=file
                        finalprintstr+=printablestr
                        finalprintstr+='\n'
        wfile = wfile.strip()
        if(write==1):
                with open(wfile, 'w') as f:
                        f.write(finalprintstr)
        elif(write==2):
                with open(wfile,'a') as f:
                        f.write(finalprintstr)
        elif(write==3):
                return finalprintstr