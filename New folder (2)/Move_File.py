import os 
import shutil
from_dir ="C:/Users/RKCC/Downloads"
to_dir = "E:/Downloads Image"
list_of_files = os.listdir(from_dir)
print(list_of_files)
for a in list_of_files:
    name,extension =os.path.splitext(a)
    print(name)
    print(extension)
    