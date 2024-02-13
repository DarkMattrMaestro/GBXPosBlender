
bl_info = {
    "name" : "GBXPos",
    "author" : "DarkMattrMaestro",
    "description" : "An addon to bring Trackmania Nations Forever to Blender and inversely.",
    "blender" : (2, 80, 0),
    "version" : (0, 0, 1),
    "location" : "",
    "warning" : "",
    "category" : "Generic"
}

import bpy


class global_vars:
    selected_file_msg:  str = "No File Selected"
    selected_video_msg: str = "No Video Selected"

    file_name:              str = None
    video_name:             str = None
    adjusted_video_name:    str = None
    replay_collection_name: str = None
    car_name:               str = None
    replay_info_object:     str = None
    camera_target:          str = None

    class loaded:
        gbx_file:       bool = False
        videoFile:      bool = False
        blocks:         bool = False
        compositing:    bool = False
        ghosts:         bool = False
        camera:         bool = False