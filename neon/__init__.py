import os
import json
import logging

class neon_config:
    def __init__(self):
        self.logger = logging.getLogger("NEON")
        try:
            logging.basicConfig(filename=os.path.expanduser("~/.neon/neon.log"))

            self.config_json = os.path.expanduser("~/.neon/config.json")
            self.config_path = os.path.expanduser("~/.neon")
            self.repo_path = os.path.expanduser("~/.neon/neon-index")
            FIRST_RUN = False
            if not os.path.isfile(self.config_json):
                os.makedirs(self.config_path, exist_ok = True)
                os.system(f"cp {os.path.join(os.path.dirname(__file__), "config_sample.json")} {self.config_json}")
                FIRST_RUN = True
            with open(self.config_json) as f:
                self.config = json.loads(f.read())
                f.close()
                if FIRST_RUN:
                    os.system(f"git clone {self.config['Index-Repo']} {self.repo_path}")
                    print("WARNING: YOU SHOULD CHANGE YOUR CONFIGURE FILE MANUALLY AT ~/.neon/config.json TO USE NEON")
                    self.logger.warning("WARNING: YOU SHOULD CHANGE YOUR CONFIGURE FILE MANUALLY AT ~/.neon/config.json TO USE NEON")
                    exit(1)
                else:
                    current_working_dir = os.getcwd()
                    os.chdir(self.repo_path)
                    os.system(f"git pull")
                    os.chdir(current_working_dir)
        except:
            self.logger.fatal("An error occured while initialization")
            os.abort()