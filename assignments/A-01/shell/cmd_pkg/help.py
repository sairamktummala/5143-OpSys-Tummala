import sys
def helpfun(commndname,write,writefile):
    if(commndname == 'pwd'):
        returnstring=""
        returnstring+=commndname
        returnstring+=":"
        returnstring+="pwd[]"
        returnstring+="\n"
        returnstring+="\t  "
        returnstring+="print the name of the current directory"
        if write == 0:
            sys.stdout.write(returnstring)
        if(write==1):
            with open(writefile, 'w') as f:
                f.write(returnstring)
        elif(write==2):
            with open(writefile,'a') as f:
                f.write(returnstring)
        elif(write==3):
            return returnstring
        
    elif(commndname == 'cat'):
        returnstring=""
        returnstring+=commndname
        returnstring+=":"
        returnstring+="cat[OPTION]... "
        returnstring+="[FILE]..."
        returnstring+="\n"
        returnstring+="Concatenate files to standard output"
        returnstring+="\n"
        returnstring+="With no FILE, or when FILE is -, read standard input"
        if write == 0:
            sys.stdout.write(returnstring)
        if(write==1):
            with open(writefile, 'w') as f:
                f.write(returnstring)
        elif(write==2):
            with open(writefile,'a') as f:
                f.write(returnstring)
        elif(write==3):
            return returnstring

    elif(commndname == 'cd'):
        returnstring=""
        returnstring+=commndname
        returnstring+=":"
        returnstring+="change the shell working directory"
        returnstring+="\n"
        returnstring+=".. is processed by removing current dir and changing to parent dir"
        if write == 0:
            sys.stdout.write(returnstring)
        if(write==1):
            with open(writefile, 'w') as f:
                f.write(returnstring)
        elif(write==2):
            with open(writefile,'a') as f:
                f.write(returnstring)
        elif(write==3):
            return returnstring

    elif(commndname == 'mkdir'):
        returnstring=""
        returnstring+=commndname
        returnstring+=":"
        returnstring+="create a directory"
        if write == 0:
            sys.stdout.write(returnstring)
        if(write==1):
            with open(writefile, 'w') as f:
                f.write(returnstring)
        elif(write==2):
            with open(writefile,'a') as f:
                f.write(returnstring)
        elif(write==3):
            return returnstring

    elif(commndname == 'mv'):
        returnstring=""
        returnstring+=commndname
        returnstring+=":"
        returnstring+="move or rename file1 to file2"
        if write == 0:
            sys.stdout.write(returnstring)
        if(write==1):
            with open(writefile, 'w') as f:
                f.write(returnstring)
        elif(write==2):
            with open(writefile,'a') as f:
                f.write(returnstring)
        elif(write==3):
            return returnstring

    elif(commndname == 'cp'):
        returnstring=""
        returnstring+=commndname
        returnstring+=":"
        returnstring+="copy file1 and call it file2"
        if write == 0:
            sys.stdout.write(returnstring)
        if(write==1):
            with open(writefile, 'w') as f:
                f.write(returnstring)
        elif(write==2):
            with open(writefile,'a') as f:
                f.write(returnstring)
        elif(write==3):
            return returnstring

    elif(commndname == 'rm'):
        returnstring=""
        returnstring+=commndname
        returnstring+=":"
        returnstring+="remove a file from directory"
        returnstring+="\n"
        returnstring+="* followed by type name removes all the files of that specific type"
        returnstring+="\n"
        returnstring+=" type* removes all the files whose name mathces with the type"
        returnstring+="\n"

        if write == 0:
            sys.stdout.write(returnstring)
        if(write==1):
            with open(writefile, 'w') as f:
                f.write(returnstring)
        elif(write==2):
            with open(writefile,'a') as f:
                f.write(returnstring)
        elif(write==3):
            return returnstring

    elif(commndname == 'rmdir'):
        returnstring=""
        returnstring+=commndname
        returnstring+=":"
        returnstring+="remove a directory"
        if write == 0:
            sys.stdout.write(returnstring)
        if(write==1):
            with open(writefile, 'w') as f:
                f.write(returnstring)
        elif(write==2):
            with open(writefile,'a') as f:
                f.write(returnstring)
        elif(write==3):
            return returnstring

    elif(commndname == 'less'):
        returnstring=""
        returnstring+=commndname
        returnstring+=":"
        returnstring+="display a file page at a time"
        if write == 0:
            sys.stdout.write(returnstring)
        if(write==1):
            with open(writefile, 'w') as f:
                f.write(returnstring)
        elif(write==2):
            with open(writefile,'a') as f:
                f.write(returnstring)
        elif(write==3):
            return returnstring

    elif(commndname == 'head'):
        returnstring=""
        returnstring+=commndname
        returnstring+=":"  
        returnstring+="display first few lines of a file if -n n lines will be printed from top of the file"
        if write == 0:
            sys.stdout.write(returnstring)
        if(write==1):
            with open(writefile, 'w') as f:
                f.write(returnstring)
        elif(write==2):
            with open(writefile,'a') as f:
                f.write(returnstring)
        elif(write==3):
            return returnstring

    elif(commndname == 'tail'): 
        returnstring=""
        returnstring+=commndname
        returnstring+=":"
        returnstring+="display last few lines of a file if -n n lines will be printed from end of the file"
        if write == 0:
            sys.stdout.write(returnstring)
        if(write==1):
            with open(writefile, 'w') as f:
                f.write(returnstring)
        elif(write==2):
            with open(writefile,'a') as f:
                f.write(returnstring)
        elif(write==3):
            return returnstring

    elif(commndname == 'grep'):
        returnstring=""
        returnstring+=commndname
        returnstring+=":"
        returnstring+="search for pattern in each filevamd if -l is given returns only the filenames which contains the pattern"
        if write == 0:
            sys.stdout.write(returnstring)
        if(write==1):
            with open(writefile, 'w') as f:
                f.write(returnstring)
        elif(write==2):
            with open(writefile,'a') as f:
                f.write(returnstring)
        elif(write==3):
            return returnstring

    elif(commndname == 'wc'):
        returnstring=""
        returnstring+=commndname
        returnstring+=":"
        returnstring+="count number of lines/characters/words in file"
        if write == 0:
            sys.stdout.write(returnstring)
        if(write==1):
            with open(writefile, 'w') as f:
                f.write(returnstring)
        elif(write==2):
            with open(writefile,'a') as f:
                f.write(returnstring)
        elif(write==3):
            return returnstring

    elif(commndname == 'sort'):
        returnstring=""
        returnstring+=commndname
        returnstring+=":"
        returnstring+="sort data in the file"
        if write == 0:
            sys.stdout.write(returnstring)
        if(write==1):
            with open(writefile, 'w') as f:
                f.write(returnstring)
        elif(write==2):
            with open(writefile,'a') as f:
                f.write(returnstring)
        elif(write==3):
            return returnstring

    elif(commndname == 'history'):
        returnstring=""
        returnstring+=commndname
        returnstring+=":" 
        returnstring+="show a history of all commands"
        if write == 0:
            sys.stdout.write(returnstring)
        if(write==1):
            with open(writefile, 'w') as f:
                f.write(returnstring)
        elif(write==2):
            with open(writefile,'a') as f:
                f.write(returnstring)
        elif(write==3):
            return returnstring

    elif(commndname == 'who'):
        returnstring=""
        returnstring+=commndname
        returnstring+=":"
        returnstring+="list users currently logged in"
        if write == 0:
            sys.stdout.write(returnstring)
        if(write==1):
            with open(writefile, 'w') as f:
                f.write(returnstring)
        elif(write==2):
            with open(writefile,'a') as f:
                f.write(returnstring)
        elif(write==3):
            return returnstring

    elif(commndname == 'chmod'):
        returnstring=""
        retutnstring+="usage :"
        returnstring+=commndname
        returnstring+=":"
        returnstring+="changes the file permissions"
        if write == 0:
            sys.stdout.write(returnstring)
        if(write==1):
            with open(writefile, 'w') as f:
                f.write(returnstring)
        elif(write==2):
            with open(writefile,'a') as f:
                f.write(returnstring)
        elif(write==3):
            return returnstring

    elif(commndname == 'exit'):
        returnstring=""
        retutnstring+="usage :"
        returnstring+=commndname
        returnstring+=":"
        returnstring+="exits from the current terminal"
        if write == 0:
            sys.stdout.write(returnstring)
        if(write==1):
            with open(writefile, 'w') as f:
                f.write(returnstring)
        elif(write==2):
            with open(writefile,'a') as f:
                f.write(returnstring)
        elif(write==3):
            return returnstring
    
    elif(commndname == 'ls'):
        returnstring=""
        retutnstring+="usage :"
        returnstring+=commndname
        returnstring+=":"
        returnstring+="returns all the files in the current directory"
        returnstring+="\n"
        returnstring+="-l gives the longlisting which includes group name username file permissions and file sizes"
        returnstring+="\n"
        returnstring+="-h gives the longlisting which includes group name username file permissions and file sizes which are human readable"
        returnstring+="\n"
        returnstring+="-a gives the files including hidden"
        returnstring+="\n"
        if write == 0:
            sys.stdout.write(returnstring)
        if(write==1):
            with open(writefile, 'w') as f:
                f.write(returnstring)
        elif(write==2):
            with open(writefile,'a') as f:
                f.write(returnstring)
        elif(write==3):
            return returnstring