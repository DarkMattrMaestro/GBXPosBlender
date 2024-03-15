
import bpy
from bpy.props import StringProperty, BoolProperty, EnumProperty

from ..utils import session_vars, constants, file_vars
from ..python_cs_interface import python_cs
from . import replay_file



class FileSelectOperatorGBXPosJSON(bpy.types.Operator):
    bl_idname = "wm.file_select"
    bl_label = "GBXPos.json File Selection Operator"
    bl_description = "Choose GBX file"
    
    use_setting: BoolProperty(
        name="Example Boolean",
        description="Example Tooltip",
        default=True,
    ) # type: ignore

    def execute(self, context):
        python_cs.GBXPosCs()
        file_vars.initial_package_file_info_json()
        replay_file.read_gbxpos_json()
        return {'FINISHED'}


importers = (
    FileSelectOperatorGBXPosJSON,
)


class ImportPanel(bpy.types.Panel):
    # Creates a Panel in the VIEW_3D UI
    bl_label = "Import"
    bl_idname = "ImportingPanel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'GBXPos'
    bl_order = 0

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.label(text="Selected GBXPos.json File:")
        
        row = layout.row()
        row.operator(FileSelectOperatorGBXPosJSON.bl_idname, text="Choose file", icon="SEQUENCE_COLOR_04" if session_vars.loaded.gbx_file else "SEQUENCE_COLOR_09")
        
        row = layout.row()
        row.label(text=session_vars.gbx_file_path.name if (session_vars.gbx_file_path is not None) else constants.Messages.NO_FILE_SELECTED, icon="FILE")
        
        row = layout.row()


classes = (
    ImportPanel,
    FileSelectOperatorGBXPosJSON,
)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)