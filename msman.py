import json
from sys import argv
import os

db = open("db.json").read()
loadedDB = json.loads(db)
rows, columns = os.popen('stty size', 'r').read().split()

class More(object):
    def __init__(self, num_lines):
        self.num_lines = num_lines
    def __ror__(self, other):
        s = str(other).replace(str(other).split("\n")[-1],"").split("\n")
        for i in range(0, len(s), self.num_lines):
            print(*s[i: i + self.num_lines], sep="\n")
            input("\033[1;30;47mEND\033[00m")

more = More(num_lines=40)  

def FormatD(description,tabsize,termsize=columns):
    lines = []
    line = []
    tabsize = " " * tabsize
    Tab = False
    descriptionarr = description.split(" ")

    for index in descriptionarr:
        line.append(index)
        if len(" ".join(line)) >= (int(termsize) - 30):
            lines.append(" ".join(line))
            line = []
    if lines == []:
        print(" ".join(line))
    else:    
        for index in lines:
            if Tab:
                print(tabsize + index)
            else:
                print(index)
            Tab = True    
    if not line == [] and Tab == True:
        print(tabsize + " ".join(line))

def GetFunc(FunctionNames,database,rlen):
    r = 1
    for function in FunctionNames:
        for i in database['functions']['function']:                                                                                                                          
            if function == i['name']:                                                                                                                     
                print('\033[1;37;40mName:\033[00m '  + i['name'])                                                                                                                           
                print('\n\033[1;37;40mDLL:\033[00m ' + i['dll'])                                                                                                                            
                print('\n\033[1;37;40mDescription:\033[00m ',end="")
                FormatD(i['description'],0)

                print('\n\033[1;37;40mArguments:\033[00m     ')                                                                                                                             
                argz = i['arguments']['argument']                                                                                                                      
                if 'dict' in str(type(argz)):                                                                                                                          
                    print('\n   \033[1;37;40mName:\033[00m ' + argz['name'])                                                                                                                
                    print('   \033[1;37;40mDescription:\033[00m ', end="")
                    FormatD(argz['description'],9)                                                                                                 
                elif 'list' in str(type(argz)): 
                    for arg in argz: 
                        print('\n   \033[1;37;40mName:\033[00m ' + arg['name']) 
                        print('   \033[1;37;40mDescription:\033[00m ',end="") 
                        FormatD(arg['description'],16)          
                print("")
                FormatD(i['returns'],0)
                break 
        if not r == rlen:        
            print("\n\n")
            r += 1
fun = argv
fun.pop(0)
GetFunc(fun,loadedDB,len(fun)) | more             
