import os
import argparse

import install
import api

parser = argparse.ArgumentParser(description = "Neon - PostgreSQL Extension Network Client")
parser.add_argument('-d', '--download', nargs = 2, help="Download an extension", metavar = ("extension", "version"))
parser.add_argument('-i', '--install', nargs = 2, help="Install an extension", metavar = ("extension", "version"))
parser.add_argument('-p', '--path', nargs = 1, help = "Specify the installtion source / Download destination", metavar = "path")

arg = parser.parse_args()

path_  = arg.path
if not arg.download == None:
    if arg.download[1] == "latest":
        arg.download[1] = "master" # the latest version is always in the master branch
    if path_ == None:
        os.makedirs(arg.download[0] + "/" + arg.download[1], exist_ok = True)
        path = os.path.join(os.getcwd(), arg.download[0] + "/" + arg.download[1])
    else:
        path = path_[0]
        os.makedirs(path, exist_ok = True)
    # try:
    api.default.download(path, arg.download[0], arg.download[1])
    # except Exception:
    #     print("Error: Extension Not Found")

if not arg.install == None:
    if path_ == None:
        path = os.path.join(os.getcwd(), arg.install[0] + "/" + arg.install[1])
    else:
        path = path_[0]
    install.install(path)