import os
import json

class neon_config:
    def __init__(self):
        self.config_json = os.path.expanduser("~/.neon/config.json")
        self.config_path = os.path.expanduser("~/.neon")
        if not os.path.isfile(self.config_json):
            os.makedirs(self.config_path, exist_ok = True)
            os.system(f"mv {os.path.join(os.path.dirname(__file__), "config_sample.json")} {self.config_json}")
        with open(self.config_json) as f:
            self.config = json.loads(f.read())
            f.close()