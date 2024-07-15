import os
import argparse
from tabulate import tabulate
import magv.default as default
import magv.pgxn as pgxn
import magv.install as install
from magv import magv_config

def search(ext, config):
    try:
        k = pgxn.search(ext, config) + default.search(ext, config)
        return k
    except Exception:
        config.logger.error(f"Failed to download {ext}")
        exit(1)

def download(path, ext, ver, source, config):
    if ver == "latest":
        ver = "master"
    try:
        if source == "MANGROVE":
            default.download(path, ext, ver, config)
        elif k[i][1] == "PGXN":
            pgxn.download(path, ext, ver, config)
    except Exception:
        config.logger.error(f"Failed to download {ext}")
        exit(1)

if __name__ == "__main__":
    config = magv_config()
    parser = argparse.ArgumentParser(description = "MANGROVE - PostgreSQL Extension Network Client")
    parser.add_argument('-s', '--search', nargs = 1, help="Search for an extension", metavar = ("extension"))
    parser.add_argument('-d', '--download', nargs = 1, help="Download an extension", metavar = ("extension"))
    parser.add_argument('-i', '--install', nargs = 1, help="Install an extension", metavar = ("extension"))
    parser.add_argument('-p', '--path', nargs = 1, help = "Specify the installtion source / Download destination", metavar = "path")

    arg = parser.parse_args()
    path_  = arg.path

    if not arg.search == None:
        print(tabulate(search(arg.search[0], config), headers=['Extension', 'Source', 'Description'], showindex="always"))

    if not arg.download == None:
        if path_ == None:
            path = os.path.join(config.config_path, arg.download[0])
        else:
            path = path_[0]
        try:
            if os.path.isdir(path):
                k = input("Folder already exists, empty the folder? (Y/n)")
                if not (k == 'n' or k == 'N'):
                    os.system(f"rm -rf {path}")
            os.makedirs(path, exist_ok = True)
        except:
            config.logger.error(f"Failed to create directories at {path}")
            exit(1)
        k = search(arg.download[0], config)
        if len(k) == 0:
            print("No extension found.")
            exit(0)
        print(tabulate(k, headers=['Extension', 'Source', 'Description'], showindex="always"))
        i = int(input(f"Which extension to download? [0 ~ {len(k)- 1}] "))
        j = input(f"Which version then? (specific version / latest) ")
        download(path, k[i][0], j, k[i][1], config)

    if not arg.install == None:
        if path_ == None:
            path = os.path.join(config.config_path, arg.install[0])
        else:
            path = path_[0]
        k = search(arg.install[0], config)
        if len(k) == 0:
            print("No extension found.")
            exit(0)
        print(tabulate(k, headers=['Extension', 'Source', 'Description'], showindex="always"))
        i = int(input(f"Which extension to install? [0 ~ {len(k)- 1}] "))
        j = input("Which version then? (specific version / latest) ")
        choice = 'n'
        if os.path.exists(path):
            choice = input(f"It seems you've already downloaded {k[i][0]}, install from local folder? (y/N) ")
        if not (choice == 'y' or choice == 'Y'):
            try:
                os.system(f"rm -rf {path}")
                os.makedirs(path, exist_ok = True)
            except:
                config.logger.error(f"Failed to create directories at {path}")
                exit(1)
            download(path, k[i][0], j, k[i][1], config)
        try:
            install.install(path, config)
        except:
            exit(1)