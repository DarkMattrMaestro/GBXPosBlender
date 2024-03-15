
import bpy, uuid, os
from bpy.app.handlers import persistent
from pathlib import Path

from ..utils import packing_json, session_vars, constants



def blend_file_data_dir() -> Path:
    """Returns the directory in the mini-fridge that is associated with the current .blend file"""
    new_path: Path = session_vars.MINI_FRIDGE_DIR.joinpath(blender_file_id())
    if (not new_path.exists()):
        print("Creating the .blend file data directory as it does not yet exist...")
        os.makedirs(new_path)
    
    return new_path
    


def blender_file_id():
    global file_info_json
    if (file_info_json is None or file_info_json[constants.FileInfoJSONComponents.BLENDER_FILE_ID_KEY] is None):
        initial_package_file_info_json()
    
    return file_info_json[constants.FileInfoJSONComponents.BLENDER_FILE_ID_KEY]


def generate_blender_file_id():
    # Generation method may change in the future, if need be.
    return uuid.uuid4().__str__()
    


@property
def replay_collection_name(self):
    raise FileNotFoundError("I may have found a bug...")

@replay_collection_name.getter
def replay_collection_name(self):
    global file_info_json
    return file_info_json[constants.FileInfoJSONComponents.REPLAY_COLLECTION_NAME_KEY]

@replay_collection_name.setter
def replay_collection_name(self, value):
    global file_info_json
    file_info_json[constants.FileInfoJSONComponents.REPLAY_COLLECTION_NAME_KEY] = value
    
    packing_json.write_json(constants.FileInfoJSONComponents.FILE_INFO_JSON_NAME, file_info_json)



file_info_json = None


@persistent
def startup_read_package_file_info_json():
    global file_info_json
    file_info_json = packing_json.read_json(constants.FileInfoJSONComponents.FILE_INFO_JSON_NAME)


def initial_package_file_info_json():
    if (not packing_json.has_json(constants.FileInfoJSONComponents.FILE_INFO_JSON_NAME)):
        global file_info_json
        file_info_json = {
            constants.FileInfoJSONComponents.BLENDER_FILE_ID_KEY: generate_blender_file_id(),
            constants.FileInfoJSONComponents.REPLAY_COLLECTION_NAME_KEY: None
        }
        packing_json.write_json(constants.FileInfoJSONComponents.FILE_INFO_JSON_NAME, file_info_json)


def register():
    bpy.app.handlers.load_post.append(startup_read_package_file_info_json)

def unregister():
    bpy.app.handlers.load_post.remove(startup_read_package_file_info_json)