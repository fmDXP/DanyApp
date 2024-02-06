while True:
    import os
    import time
    import shutil

    y = input("Welcome to the DanyApp Installer V1.0: Do you want to install DanyApp DEV? (y/n)")

    if y == "y":

        print("Installing...")

        os.chdir("C:\\")

        Dest = "C:\DanyApp"
        shutil.copytree("C:/DanyAppInst/InstallerData", Dest)

        print("Installation Done! (you may close this window...)")
        time.sleep(3)
        quit()
        
    elif y == "n":
        quit()


    else:
        print("DanyApp/installer.py: Error 1")
        time.sleep(5)
        quit()


