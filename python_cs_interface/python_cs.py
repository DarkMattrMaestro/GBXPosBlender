
import os

from ..utils import session_vars



def GBXPosCs():
    lastCWD = os.getcwd()
    
    os.chdir(session_vars.CS_DIR)
    os.system("GBXPos")
    
    os.chdir(lastCWD)