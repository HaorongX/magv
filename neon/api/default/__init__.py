__all__ = ["download", "search"]

import api.default.gitrepo
import requests
import json
import base64
import os

def INDEX_SERVICE(ext):
    with open(os.path.join(__path__[0], "config.json"), "r") as f:
        token = json.loads(f.read())["Auth-Token"]
        f.close()
    req = requests.get("https://api.atomgit.com/repos/haorongxu/neon-index/contents/index.json", headers = {"Authorization":f"Bearer {token}"})
    if not req.status_code == 200:
        raise Exception("Error: Unable to locate given extension")
    b64str = json.loads(req.content)["content"]
    return json.loads(base64.b64decode(b64str))[ext]

def download(path, ext, ver):
    api.default.gitrepo.download(path, INDEX_SERVICE(ext), ver)

def search(ext):
    with open(os.path.join(__path__[0], "config.json"), "r") as f:
        token = json.loads(f.read())["Auth-Token"]
        f.close()
    req = requests.get("https://api.atomgit.com/repos/haorongxu/neon-index/contents/index.json", headers = {"Authorization":f"Bearer {token}"})
    if not req.status_code == 200:
        raise Exception("Error: Unable to locate given extension")
    dist = json.loads(base64.b64decode(json.loads(req.content)["content"]))
    res = list()
    for i in dist:
        if not i.find(ext) == -1:
            res.append([i, "Default"])
    return res