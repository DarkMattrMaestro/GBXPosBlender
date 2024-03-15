
import bpy, ctypes, os
from pathlib import Path



PARENT_DIR = Path(__file__).parent.parent

CS_DIR: Path = PARENT_DIR.joinpath("GBXPos", "GBXPos", "bin", "Debug")

MINI_FRIDGE_DIR: Path = PARENT_DIR.joinpath("mini_fridge")
if not MINI_FRIDGE_DIR.exists():
    print("Creating mini fridge directory as it does not yet exist...")
    os.mkdir(MINI_FRIDGE_DIR)


gbx_file_path:          Path = None
video_file_path:        Path = None
adjusted_video_Path:    Path = None

car_name:               str = None
replay_info_object:     str = None
camera_target:          str = None

class loaded:
    gbx_file:       bool = False
    video_file:     bool = False
    blocks:         bool = False
    compositing:    bool = False
    ghosts:         bool = False
    camera:         bool = False

