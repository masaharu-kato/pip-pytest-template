"""
    My example Module (extra module)
"""
from typing import Optional
from . import mycalc

def myexadd(a, b) -> Optional[int]:
    try:
        a_int = int(a)
        b_int = int(b)
    except ValueError:
        return None
    
    return mycalc.myadd(a_int, b_int)
