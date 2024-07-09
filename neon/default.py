import neon.gitrepo as gitrepo
import requests
import json
import base64

def INDEX_SERVICE(ext, config):
    token = config["Auth-Token"]
    req = requests.get("https://api.atomgit.com/repos/haorongxu/neon-index/contents/index.json", headers = {"Authorization":f"Bearer {token}"})
    if not req.status_code == 200:
        raise Exception("Error: Unable to locate given extension")
    b64str = json.loads(req.content)["content"]
    return json.loads(base64.b64decode(b64str))[ext]

def download(path, ext, ver, config):
    gitrepo.download(path, INDEX_SERVICE(ext, config), ver)

def search(ext, config):
    token = config["Auth-Token"]
    req = requests.get("https://api.atomgit.com/repos/haorongxu/neon-index/contents/index.json", headers = {"Authorization":f"Bearer {token}"})
    if not req.status_code == 200:
        raise Exception("Error: Unable to locate given extension")
    dist = json.loads(base64.b64decode(json.loads(req.content)["content"]))
    res = list()
    for i in dist:
        if not i.find(ext) == -1:
            res.append([i, "Default"])
    return res
