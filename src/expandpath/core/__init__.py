from typing import *
import os

__all__ = ["expandpath"]

def expandpath(value:Any, /)->Any:
    "This function expands a given path."
    ans = os.path.expanduser(value)
    ans = os.path.expandvars(ans)
    return ans