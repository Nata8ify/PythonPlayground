import glob

import os


class Main():
    print(glob.glob("/*.*")) # listing all file in / (root) of project partition.
    print(glob.glob("D:\8ight\MO\*.dll")) # listing file in D:\8ight\MO\*.dll.
    print(os.listdir("/")) # listing directory / (root) of project partition.
    print(os.getcwd()) # printing current directory.
    print(os.path.dirname(os.path.abspath(__file__))) # printing current directory (script file being run).
    print(glob.glob(os.getcwd()+"/*.py")) # listing all file in current directory which is .py.


if __name__ == "__main__" :
    Main()