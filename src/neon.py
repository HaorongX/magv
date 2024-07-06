import os
import argparse
import importlib

parser = argparse.ArgumentParser(description = "Neon - PostgreSQL Extension Network Client")
parser.add_argument('-a', '--api', nargs = 1, help="Specify which API to use", metavar = ("API"))
parser.add_argument('-d', '--download', nargs = 2, help="Download an extension", metavar = ("extension", "version"))
parser.add_argument('-i', '--install', nargs = 2, help="Install an extension", metavar = ("extension", "version"))
parser.add_argument('-p', '--path', nargs = 1, help = "Specify the installtion source / Download destination", metavar = "path")

arg = parser.parse_args()
if not arg.api == None:
    api = importlib.import_module(arg.api[0])
else:
    api = importlib.import_module("default")

path_  = arg.path
if not arg.download == None:
    if path_ == None:
        os.makedirs(arg.download[0] + "/" + arg.download[1], exist_ok = True)
        path = os.path.join(os.getcwd(), arg.download[0] + "/" + arg.download[1])
    else:
        path = path_[0]
        os.makedirs(path, exist_ok = True)
    try:
        api.download(path, arg.download[0], arg.download[1])
    except Exception:
        print("Error: Extension Not Found")

if not arg.install == None:
    if path_ == None:
        path = os.path.join(os.getcwd(), arg.install[0] + "/" + arg.install[1], arg.install[0] + "-" + arg.install[1])
    else:
        path = path_[0]
    api.install(path, arg.install[0], arg.install[1])