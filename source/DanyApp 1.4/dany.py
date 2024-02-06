import os
import os.path
import subprocess
import shutil
from danyconf import Dependecies

class DanyApp:
    class func:
        class Dany:

            def check(file):

                    f = file

                    if f == "":
                        print("DanyApp Error: 1")
                    
                    else:
                        ff = open(f,"r")
                        fr = ff.read()
                        print(fr)


            def dir(self):
                s = self
                os.chdir(s)

            def cls():
                os.chdir("C:\\DanyApp\Clean")
                subprocess.call("cls.bat")

            def ver():
                print("DanyAppDEV Version:  ",DanyCONF.DanyAppVersion)

            def DanyConf(conf):
                x = "init"
                if conf == x:
                    if DanyCONF.Color == "red":
                        DanyFS.color("red")
                    elif DanyCONF.Color == "blue":
                        DanyFS.color("blue")
                    elif DanyCONF.Color == "yellow":
                        DanyFS.color("yellow")
                    elif DanyCONF.Color == "green":
                        DanyFS.color("green")
                    elif DanyCONF.Color == "norm":
                        DanyFS.color("norm")
                    elif DanyCONF.LoadDirectory == True:
                        DanyFS.dir(DanyCONF.StartUpDir)


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
       
DanyFS = DanyApp.func.Dany
DanyCONF = Dependecies