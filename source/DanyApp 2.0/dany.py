import os
import os.path
import subprocess
import shutil
import time
from subprocess import Popen, CREATE_NEW_CONSOLE

class DanyApp:
    class func:
        class Dany:

            def printFile(file):

                    if file == "":
                        print("DanyApp Error: 1")
                    
                    else:
                        ff = open(file,"r").read()
                        print(ff)


            def dir(self):
                os.chdir(self)

            def cls():
                os.chdir("C:\\DanyApp\Clean")
                subprocess.call("cls.bat")


            def color(color):
                colorlist = ["red","blue","yellow","green","norm"]
                if color == "":
                    print("DanyApp Error: 2")
                    
                else:
                    if color in colorlist:
                        if color == "yellow":
                            os.chdir("C:\\DanyApp\Colors")
                            subprocess.call("yellow.bat")
                            os.chdir("C:\\")
                        elif color == "red":
                            os.chdir("C:\\DanyApp\Colors")
                            subprocess.call("red.bat")
                            os.chdir("C:\\")
                        elif color == "blue":
                            os.chdir("C:\\DanyApp\Colors")
                            subprocess.call("blue.bat")
                            os.chdir("C:\\")
                        elif color == "green":
                            os.chdir("C:\\DanyApp\Colors")
                            subprocess.call("green.bat")
                            os.chdir("C:\\")
                        elif color == "norm":
                            os.chdir("C:\\DanyApp\Colors")
                            subprocess.call("norm.bat")
                            os.chdir("C:\\")
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
                
                
                
dany = DanyApp.func.Dany