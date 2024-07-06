import os

def download(path, extension, ver):
    os.chdir(path)
    os.system("git clone --depth=1 --branch " + ver + " " + extension + " " + path)

def install(path, extension, ver):
    os.chdir(path)
    if os.path.isfile("autogen.sh"):
        os.system("sh ./autogen.sh")
    if os.path.isfile("configure"):
        os.system("./configure")
    os.system("make")
    os.system("make install")