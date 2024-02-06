import os
import shutil
import time
from subprocess import Popen, CREATE_NEW_CONSOLE

class dany():

            def printFile(file):

                    if file == "":
                        print("DanyApp Error: 1")
                    
                    else:
                        ff = open(file,"r").read()
                        print(ff)


            def dir(self):
                os.chdir(self)


            def cls():
                os.system("cls")


            def color(color):
                colorlist = ["red","blue","yellow","green","norm"]
                if color == "":
                    print("DanyApp Error: 2")
                    
                else:
                    if color in colorlist:
                        if color == "yellow":
                            os.system("color 0E")
                            
                        elif color == "red":
                            os.system("color 0C")
                            
                        elif color == "blue":
                            os.system("color 09")
                            
                        elif color == "green":
                            os.system("color 02")
                            
                        elif color == "norm":
                            os.system("color")
                    else:
                        print("DanyApp Error: 3")


            def copy(x,y):
                if x == "":
                    print("DanyApp Error: 4")
                
                else:
                    if y == "":
                        print("DanyApp Error: 5")
                    
                    else:
                        shutil.copy(x,y)


            def move(x,y):
                if x == "":
                    print("DanyApp Error: 6")

                else:
                    if y == "":
                        print("DanyApp Error: 7")
                    
                    else:
                        shutil.move(x,y)


            def is_file(x):
                if x == "":
                    print("DanyApp Error: 8")
                
                else:
                    if os.path.isfile(x) == True:
                        return True
                    else:
                        return False
                   
                    
            def is_folder(x):
                if x == "":
                    print("DanyApp Error: 9")
                
                else:
                    if os.path.exists(x) == True:
                        return True
                    else:
                        return False
       
            

            def error(errNum, text, type):
    
                Critical = ["Critical","critical","crit"]
                Normal = ["Normal","normal","norm"]
                Warning = ["Warning","warning","warn"]
                Notice = ["Notice","notice","note"]
    
                global fine
                fine = None
    
    
                if type in Critical:
        
                    fine = f"Critical Error! {text} Error Code: {errNum}"
        
    
                elif type in Normal:
        
                    fine = f"Error! {text} Error Code: {errNum}"
    
    
                elif type in Warning:
        
                    fine = f"Warning! {text}"
    
    
                elif type in Notice:
        
                    fine = f"Notice! {text}"
    
    
    
                else:
                    print(f"DanyApp Error: 14")
        
        
                return fine


## VI's ---> V = Var   I = In  // File Format


            def viText(var, fileName):
    
                if var != "":
        
                    file = open(fileName+".txt","w+").write(var)
                    file
        
                else:
                    print("DanyApp Error: 13")
        
        
        

            def viBat(var, fileName):
    
                if var != "":
        
                    file = open(fileName+".bat","w+").write(var)
                    file
        
                else:
                    print("DanyApp Error: 12")
                    
                    
            
            def viEXT(var, fileName, ext):
    
                if var != "":
        
                    file = open(fileName+ext,"w+").write(var)
                    file
        
                else:
                    print("DanyApp Error: 15")
        
        
### - - -      
                
            def run(path):
    
                if os.path.isfile(path):
        
                    Popen(path, creationflags=CREATE_NEW_CONSOLE)
    
                else:
                    print("DanyApp Error: 11")
                    
                    
                    
            def sub(path):
    
                if os.path.isfile(path):
        
                    Popen(path)
    
                else:
                    print("DanyApp Error: 11")
                    
                    
            def delFile(path):
                
                if os.path.isfile(path):
                    
                    os.remove(path)
                    
                else:
                    print("DanyApp Error: 10")
                
                    
            def wait(sec):             
                time.sleep(sec)
                
                
            def taskkill(task):
                
                try:
                    os.system(f"taskkill {task}")
                    
                except Exception as e:
                    print(f"DanyApp Error: 16 ({e})")

                    
                    
            def taskstart(task):
                
                try:
                    os.system(f"start {task}")
                    
                except Exception as e:
                    print(f"DanyApp Error: 17 ({e})")
                
                
                
            def Mpower(base,exp):
                return base ** exp
            
            
            def Msquare_root(num):
                return num ** 0.5
            
            
            def Mcubic_root(num):
                return num ** (1/3)

            