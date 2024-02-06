import os
class DanyApp:
    class func:
        class Dany:
            
            
            def check(file):

                    f = file

                    if f == "":
                        print("DanyApp Error: 0")

                    else:
                        ff = open(f,"r")
                        fr = ff.read()
                        print(fr)


            def dir(self):
                s = self
                os.chdir(s)



       
                 

DanyFS = DanyApp.func.Dany