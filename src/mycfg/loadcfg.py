"""
    My example Module (with extra public module)
"""

import yaml

def loadcfg(path):
    with open(path, mode='r') as f:
        return yaml.load(f, Loader=yaml.SafeLoader)
