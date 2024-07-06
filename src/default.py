import os
import gitrepo
import requests
import json
import base64

def INDEX_SERVICE(ext):
    with open("config.json", "r") as f:
        token = json.loads(f.read())["Auth-Token"]
        f.close()
    req = requests.get("https://api.atomgit.com/repos/haorongxu/neon-index/contents/index.json", headers = {"Authorization":f"Bearer {token}"})
    if not req.status_code == 200:
        raise Exception("Error: Unable to locate given extension")
    b64str = json.loads(req.content)["content"]
    return json.loads(base64.b64decode(b64str))[ext]

def download(path, ext, ver):
    gitrepo.download(path, INDEX_SERVICE(ext), ver)

def install(arg1, arg2, arg3):
    gitrepo.install(arg1, arg2, arg3)