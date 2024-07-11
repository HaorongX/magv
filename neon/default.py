import neon.gitrepo as gitrepo
from neon import neon_config
import json
import os

def download(path, ext, ver, config):
    # try:
    with open(os.path.join(config.repo_path, f"{ext}.json"), "r") as f:
        repo = json.loads(f.read())["repo"]
        f.close()
    # except Exception:
        # raise Exception("FATAL: Extension not found!")
    gitrepo.download(path, repo, ver)

def search(ext, config):
    dist = os.listdir(config.repo_path)
    res = list()
    for i in dist:
        if not i.find(ext) == -1:
            res.append([i.rsplit(".", 1)[0], "Default"]) # Strip the ".json" part
    return res