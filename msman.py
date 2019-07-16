import json
from sys import argv

db = open("db.json").read()
loadedDB = json.loads(db)

class More(object):
    def __init__(self, num_lines):
        self.num_lines = num_lines
    def __ror__(self, other):
        s = str(other).replace(str(other).split("\n")[-1],"").split("\n")
        for i in range(0, len(s), self.num_lines):
            print(*s[i: i + self.num_lines], sep="\n")
            input("\033[1;30;47mEND\033[00m")

more = More(num_lines=40)  

def GetFunc(FunctionNames,database,rlen):
    r = 1
    for function in FunctionNames:
        for i in database['functions']['function']:                                                                                                                          
            if function in i['name']:                                                                                                                     
                print('\033[1;37;40mName:\033[00m '  + i['name'])                                                                                                                           
                print('\n\033[1;37;40mDLL:\033[00m ' + i['dll'])                                                                                                                            
                print('\n\033[1;37;40mDescription:\033[00m ',end="")
                if len(i['description']) > 110:
                   si = i['description'].split(" ")
                   li = int(len(si) / 2)
                   si[li] = si[li] + "\n            "
                   print(" ".join(si))
                else:
                    print(i['description'])

                print('\n\033[1;37;40mArguments:\033[00m     ')                                                                                                                             
                argz = i['arguments']['argument']                                                                                                                      
                if 'dict' in str(type(argz)):                                                                                                                          
                    print('\n   \033[1;37;40mName:\033[00m ' + argz['name'])                                                                                                                
                    print('   \033[1;37;40mDescription:\033[00m ', end="")
                    if len(argz['description']) > 110:
                        si = argz['description'].split(" ")
                        li = int(len(si) / 2)
                        si[li] = si[li] + "\n               "
                        print(" ".join(si))
                    else:
                        print(argz['description'])                                                                                                   
                elif 'list' in str(type(argz)): 
                    for arg in argz: 
                        print('\n   \033[1;37;40mName:\033[00m ' + arg['name']) 
                        print('   \033[1;37;40mDescription:\033[00m ',end="") 
                        if len(arg['description']) > 110:
                            si = arg['description'].split(" ")
                            li = int(len(si) / 2)
                            si[li] = si[li] + "\n               "
                            print(" ".join(si))
                        else:
                            print(arg['description'])           
                print('\n' + i['returns'],end="")         
                break 
        if not r == rlen:        
            print("\n\n")
            r += 1
fun = argv
fun.pop(0)
GetFunc(fun,loadedDB,len(fun)) | more             
