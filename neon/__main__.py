import os
import argparse
from tabulate import tabulate
import neon.default as default
import neon.pgxn as pgxn
import neon.install as install
from neon import neon_config

neon_config = neon_config()

parser = argparse.ArgumentParser(description = "Neon - PostgreSQL Extension Network Client")
parser.add_argument('-s', '--search', nargs = 1, help="Search for an extension", metavar = ("extension"))
parser.add_argument('-d', '--download', nargs = 2, help="Download an extension", metavar = ("extension", "version"))
parser.add_argument('-i', '--install', nargs = 1, help="Install an extension", metavar = ("extension"))
parser.add_argument('-p', '--path', nargs = 1, help = "Specify the installtion source / Download destination", metavar = "path")

arg = parser.parse_args()
path_  = arg.path

def search(ext):
    k = pgxn.search(ext) + default.search(ext, neon_config.config)
    return k

if not arg.search == None:
    print(tabulate(search(arg.search[0]), headers=['Extension', 'Source'], showindex="always"))

if not arg.download == None:
    if arg.download[1] == "latest":
        arg.download[1] = "master" # the latest version is always in the master branch
    if path_ == None:
        path = os.path.join(neon_config.config_path, arg.download[0])
    else:
        path = path_[0]
    os.makedirs(path, exist_ok = True)
    k = search(arg.download[0])
    print(tabulate(k, headers=['Extension', 'Source'], showindex="always"))
    i = int(input(f"Which extension to download? [0 ~ {len(k)- 1}]"))
    if k[i][1] == "Default":
        default.download(path, k[i][0], arg.download[1], neon_config.config)
    elif k[i][1] == "PGXN":
        pgxn.download(path, k[i][0], arg.download[1])

if not arg.install == None:
    if path_ == None:
        path = os.path.join(neon_config.config_path, arg.install[0])
    else:
        path = path_[0]
    install.install(path)