import json
import os
from pathlib import Path


class Config():
    def __init__(self, name):
        self.name = name
        self._config = {}
        self._path = "{}/.{}".format(Path.home(), name)

    def _read_file(self):
        try:
            with open( self._path, "r" ) as f:
                contents = f.read()
                self._config = json.loads(contents)
        except:
            pass
    def load_profile(self, profile):
        self._read_file()        
        try:
            return self._config['profile']
        except IndexError:
            return self._config

    def load_all_profiles(self):
        return self._read_file()

    def write_config(self, config=None):
        if config is not None:
            self._config = config
        with open ( self._path, "w" ) as f:
           json_config = json.dumps(self._config)
           f.write(json_config)
           os.chmod(0o600)