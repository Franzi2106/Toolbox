# core/config/config_manager.py

####### MEIN CODE ######
# core/config/config_manager.py

import os
from configparser import ConfigParser

class ConfigManager:
    def __init__(self, path):
        self.path = path
        self.cfg  = ConfigParser()
        # default settings
        self.cfg["APP"] = {
            "show_config_on_startup": "False",
            "n_procs": "2",
            "subject_id": ""
        }

        self.cfg["PATHS"] = {
            "output_dir": "./results",
            "bids_root": "",
            "atlas_path": "",
            "reference_T1": "",
            "moving_image": ""
            
        }

        self.cfg["FSL"] = {
            "singularity_image": "/cvmfs/neurodesk.ardc.edu.au/containers/fsl_6.0.4_20210105/fsl_6.0.4_20210105.simg"
        }
        if os.path.exists(path):
            self.cfg.read(path)
        else:
            with open(path, "w") as f:
                self.cfg.write(f)

    def get(self, section, option, fallback=None):
        return self.cfg.get(section, option, fallback=fallback)

    def getboolean(self, section, option, fallback=None):
        return self.cfg.getboolean(section, option, fallback=fallback)

    def getint(self, section, option, fallback=None):
        return self.cfg.getint(section, option, fallback=fallback)

    def __str__(self):
        from io import StringIO
        buf = StringIO()
        self.cfg.write(buf)
        return buf.getvalue()

    def save(self):
        with open(self.path, "w") as f:
            self.cfg.write(f)
