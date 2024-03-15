
import bpy, json, os, math
from pathlib import Path

from ..python_cs_interface import python_cs
from ..utils import file_vars, session_vars, message_utils



def read_gbxpos_json():
    print("running ReadGBXPosJSON...")
    
    # For simplicity's sake, C# sends the replay to the mini-fridge, then Python picks it up and moves it to the specific blend file data directory.
    cs_replay_file_path = session_vars.MINI_FRIDGE_DIR.joinpath("NewReplay.json")
    replay_file_path = file_vars.blend_file_data_dir().joinpath("replay.json")
    
    if not (cs_replay_file_path.is_file): # If GBXPosCS did not load a replay, 
        raise FileNotFoundError("File \"" + cs_replay_file_path + "\" was not found in the mini fridge. Something went wrong.")
    
    os.replace(cs_replay_file_path, replay_file_path)
    
    f = open(replay_file_path)
    session_vars.replay_info_object = json.load(f)["Node"]
    f.close()
    
    message_utils.show_message_box(title=str(replay_file_path),icon="FILE",lines=str(session_vars.replay_info_object))# Show tooltip with selected file information
    
    session_vars.gbx_file_path = replay_file_path
    
    session_vars.loaded.gbx_file = True
    
    
    # Delete default collection
    defaultCollection = bpy.data.collections.get("Collection")
    if (defaultCollection):
        bpy.data.collections.remove(defaultCollection)
    
    # Create new collection
    replayCollection = bpy.data.collections.new(session_vars.gbx_file_path.name)
    bpy.context.scene.collection.children.link(replayCollection)
    file_vars.replay_collection_name = replayCollection.name
    
    # Set scene defaults
    bpy.context.scene.render.fps = 1
    bpy.context.scene.render.fps_base = 1
    bpy.context.scene.render.engine = "BLENDER_EEVEE"
    bpy.context.scene.render.film_transparent = True
    bpy.context.scene.render.use_motion_blur = True
    #bpy.context.scene.render.motion_blur_shutter = 1
    
    sun = bpy.data.lights.new(name="GBXPosSun",type="SUN")
    sun.angle = math.radians(3)
    sunObject = bpy.data.objects.new("GBXPosSun", sun)
    bpy.data.collections[file_vars.replay_collection_name].objects.link(sunObject)
    sunObject.rotation_euler.x = math.degrees(45)
    sunObject.rotation_euler.y = math.degrees(-21)
    
    bpy.ops.wm.redraw_timer(type='DRAW_WIN_SWAP', iterations=1)
    return

