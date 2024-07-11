import os
import requests
import shutil
import json

PGXN_API = "https://api.pgxn.org"
def download(path, extension, version):
    obj = requests.get(PGXN_API + f"/dist/{extension}/{version}/{extension}-{version}.zip")
    if not obj.status_code == 200:
        raise Exception(obj.status_code)
    with open(os.path.join(path, f"{extension}-{version}.zip"), "wb+") as f:
        f.write(obj.content)
    f.close()
    shutil.unpack_archive(os.path.join(path, f"{extension}-{version}.zip"), path)
    os.system(f"mv {os.path.join(path, f'{extension}-{version}')}/* {path}")
    os.removedirs(os.path.join(path, f"{extension}-{version}"))
    os.remove(os.path.join(path, f.name))

def search(ext):
    res = json.loads(requests.get(f"https://api.pgxn.org/search/extensions?q={ext}").content)["hits"]
    ext_list = list()
    for item in res:
        ext_list.append([item["extension"], "PGXN", item["abstract"]])
    return ext_list