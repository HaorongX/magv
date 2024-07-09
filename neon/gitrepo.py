import os

def download(path, extension, ver):
    os.chdir(path)
    os.system("git clone --depth=1 --branch " + ver + " " + extension + " " + path)
