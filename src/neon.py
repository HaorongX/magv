import os
import argparse
import requests
import zipfile

parser = argparse.ArgumentParser(description = "Neon - PostgreSQL Extension Network Client")
parser.add_argument('-d', '--download', nargs = 2, help="Download an extension", metavar = ("extension", "version"))
parser.add_argument('-i', '--install', nargs = 2, help="Install an extension", metavar = ("extension", "version"))
parser.add_argument('-p', '--path', nargs = 1, help = "Specify the installtion source / Download destination", metavar = "path")

arg = parser.parse_args()

path_  = arg.path
if not arg.download == None:
    res = requests.get("http://127.0.0.1:5000/archives/" + arg.download[0] + "/" + arg.download[1])
    if not res.status_code == 200:
        exit(1)
    if path_ == None:
        os.makedirs(arg.download[0] + "/" + arg.download[1], exist_ok = True)
        path = os.path.join(os.getcwd(), arg.download[0] + "/" + arg.download[1])
    else:
        path = path_[0]
        os.makedirs(path, exist_ok = True)
    with open(os.path.join(path, arg.download[0] + "-" + arg.download[1] + ".zip"),'wb') as f:
        f.write(res.content)

if not arg.install == None:
    if path_ == None:
        path = os.path.join(os.getcwd(), arg.install[0] + "/" + arg.install[1], arg.install[0] + "-" + arg.install[1])
    else:
        path = path_[0]
    if os.path.isfile(os.path.join(path, "configure")):
        os.system(os.path.join(path, "configure"))
    os.chdir(path)
    os.system("make")
    os.system("make install")