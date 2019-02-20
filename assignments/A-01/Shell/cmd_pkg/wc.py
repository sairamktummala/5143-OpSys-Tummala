import sys
import os
 
def wcfun(cmd):
        if(len(cmd)>2):
                wcfun2(cmd)
        else:
                wcfun1(cmd[1])



def wcfun1(file):
        countLines = 0
        countWords = 0
        count_char = 0
        if os.path.exists(file):    
                with open(file) as var:
                        lines=var.readlines()
                with open(file) as data:
                        for line in data:
                                line = line.strip(' ')
                                count_char += len(line)
                                words=line.split()
                                countWords += len(words)
                                count_char+=1 
                #count_char -= 1         
                #count_Lines = len(lines) - 1
                count_Lines = len(lines)
                sys.stdout.write('  ')
                sys.stdout.write(str(count_Lines))
                sys.stdout.write(' ')
                sys.stdout.write(str(countWords))
                sys.stdout.write(' ')
                sys.stdout.write(str(count_char))
                sys.stdout.write(' :')
                sys.stdout.write(file)
                sys.stdout.write('\n')    
             

        else:
                sys.stdout.write(file)
                sys.stdout.write(': No such file exists \n')


def wcfun2(cmd):
        countLines = 0
        countWords = 0
        count_char = 0
        if os.path.exists(cmd[2]):
                with open(cmd[2]) as var:
                        lines=var.readlines()
                with open(cmd[2]) as data:
                        for line in data:
                                line = line.strip(' ')
                                count_char += len(line)
                                words=line.split()
                                countWords += len(words)
                                count_char+=1  
                #count_char -= 1         
                #count_Lines = len(lines) - 1
                count_Lines = len(lines)
                count_Lines = len(lines)
                if cmd[1] == '-l':
                        sys.stdout.write(str(count_Lines))
                        sys.stdout.write(' :  ')
                        sys.stdout.write(str(cmd[2]))
                        sys.stdout.write('\n')
                elif cmd[1] == '-w':
                        sys.stdout.write(str(countWords))
                        sys.stdout.write(' :  ')
                        sys.stdout.write(str(cmd[2]))
                        sys.stdout.write('\n')
                elif cmd[1] == '-m':
                        sys.stdout.write(str(count_char))
                        sys.stdout.write(' :  ')
                        sys.stdout.write(str(cmd[2]))
                        sys.stdout.write('\n')
                else:
                        sys.stdout.write('flag not recognised')
        else:
                sys.stdout.write(str(cmd[1]))
                sys.stdout.write(': No such file exists \n')


#write starts here
def wcfunwrite(cmd,write,writefile):
        if(len(cmd)>2):
                wcfun2write(cmd,write,writefile)
        else:
                wcfun1write(cmd[1],write,writefile)



def wcfun1write(file,write,writefile):
        countLines = 0
        countWords = 0
        count_char = 0
        retstring=""
        if os.path.exists(file):    
                with open(file) as var:
                        lines=var.readlines()
                with open(file) as data:
                        for line in data:
                                line = line.strip()
                                count_char += len(line)
                                words=line.split()
                                countWords += len(words)
                                count_char+=1 
                #count_char -= 1         
                #count_Lines = len(lines) - 1
                count_Lines = len(lines)
                retstring+='  '
                retstring+=str(count_Lines)
                retstring+=' '
                retstring+=str(countWords)
                retstring+=' '
                retstring+=str(count_char)
                retstring+=' :'
                retstring+=file
                retstring+='\n'  
                writefile=writefile.strip()
                if(write==1):
                        with open(writefile, 'w') as f:
                                f.write(retstring)
                elif(write==2):
                        with open(writefile,'a') as f:
                                f.write(retstring)
                elif(write==3):
                        return retstring
     

        else:
                sys.stdout.write(file)
                sys.stdout.write(': No such file exists \n')


def wcfun2write(cmd,write,writefile):
        countLines = 0
        countWords = 0
        count_char = 0
        returnstrin=""
        if os.path.exists(cmd[2]):
                with open(cmd[2]) as var:
                        lines=var.readlines()
                with open(cmd[2]) as data:
                        for line in data:
                                count_char += len(line)
                                words=line.split()
                                countWords += len(words)
                                count_char+=1  
                #count_char -= 1         
                #count_Lines = len(lines) - 1
                count_Lines = len(lines)
                if cmd[1] == '-l':
                        returnstrin+=str(count_Lines)
                        returnstrin+=' :  '
                        returnstrin+=str(cmd[2])
                        returnstrin+='\n'
                elif cmd[1] == '-w':
                        returnstrin+=str(countWords)
                        returnstrin+=' :  '
                        returnstrin+=str(cmd[2])
                        returnstrin+='\n'
                elif cmd[1] == '-m':
                        returnstrin+=str(count_char)
                        returnstrin+=' :  '
                        returnstrin+=str(cmd[2])
                        returnstrin+='\n'
                writefile=writefile.strip()
                if(write==1):
                        with open(writefile, 'w') as f:
                                f.write(returnstrin)
                elif(write==2):
                        with open(writefile,'a') as f:
                                f.write(returnstrin)
                elif(write==3):
                        return returnstrin

        else:
                sys.stdout.write(str(cmd[1]))
                sys.stdout.write(': No such file exists \n')