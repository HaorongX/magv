import os
import requests
import zipfile

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