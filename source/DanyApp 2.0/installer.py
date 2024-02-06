while True:
    import os.path
    import time
    import shutil


    def viBat(var, fileName):
    
                if var != "":
        
                    file = open(fileName+".bat","w+").write(var)
                    file
        
                else:
                    print("DanyApp Installer Error: 1")
    
    
    cls = """
    @echo off\n
    cls"""
    
    blue = """
    @echo off\n
    color 09"""
    
    green = """
    @echo off\n
    color 02"""
    
    norm = """
    @echo off\n
    color 0F"""
    
    red = """
    @echo off\n
    color 0C"""
    
    yellow = """
    @echo off\n
    color 0E"""
    
    
    x = input("DanyApp Installer Do you want to install DanyApp? (Y/n)")

    if x == "y" or "Y" or "":

        print("\nInstalling...")

        
        if os.path.exists("C:/DanyApp"):
            print("\nDanyApp Installer: Error: 3")
            
        else:
            
            os.mkdir("DanyApp")
            os.mkdir("DanyApp\Colors")
            os.mkdir("DanyApp\Clean")
            
            viBat(cls,"cls")
            viBat(blue,"blue")
            viBat(green,"green")
            viBat(norm,"norm")
            viBat(red,"red")
            viBat(yellow,"yellow")
            
            shutil.move("cls.bat","DanyApp\Clean")
            shutil.move("blue.bat","DanyApp\Colors")
            shutil.move("green.bat","DanyApp\Colors")
            shutil.move("norm.bat","DanyApp\Colors")
            shutil.move("red.bat","DanyApp\Colors")
            shutil.move("yellow.bat","DanyApp\Colors")
            
            shutil.move("DanyApp","C:\\")
            

            print("\nInstallation Done! (you may close this window...)")
            time.sleep(3)
            quit()
        
    elif x == "n" or "N":
        quit()


    else:
        print("\nDanyApp Installer: Error 2")
        time.sleep(5)
        break


quit()