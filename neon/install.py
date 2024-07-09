import os

def install(path):
    if not os.getuid() == 0:
        print("WARNING: You are trying to install an extension without sudo")
    # try:
    os.chdir(path)
    if os.path.isfile("autogen.sh"):
        os.system("sh ./autogen.sh")
    if os.path.isfile("configure"):
        os.system("./configure")
    os.system("make")
    os.system("make install")
    # except Exception as e:
    #     print("Installation failed: ", e.__cause__)