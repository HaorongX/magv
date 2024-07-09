__all__ = ["download", "search"]

import os
import requests
import zipfile
import json

PGXN_API = "https://api.pgxn.org"
def download(path, extension, version):
    obj = requests.get(PGXN_API + f"/dist/{extension}/{version}/{extension}-{version}.zip")
    if not obj.status_code == 200:
        raise Exception(obj.status_code)
    with open(os.path.join(path, f"{extension}-{version}.zip"), "wb+") as f:
        f.write(obj.content)
    f.close()
    archive = zipfile.ZipFile(os.path.join(path, f.name), "r")
    archive.extractall(path = path)
    archive.close()

def search(ext):
    res = json.loads(requests.get(f"https://api.pgxn.org/search/extensions?q={ext}").content)["hits"]
    ext_list = list()
    for item in res:
        ext_list.append([item["extension"], "PGXN"])
    return ext_list