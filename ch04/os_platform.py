import os
import pathlib
import platform

myfolder = pathlib.Path.cwd()
print(myfolder)
myfile = myfolder/'files'/'example.txt'
print(myfile)
if platform.system() == "Windows":
    os.system(f"explorer {myfile}") 
elif platform.system() == "Darwin":
    os.system(f"open {myfile}") 
else:
    os.system(f"xdg-open {myfile}") 

