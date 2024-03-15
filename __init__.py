
bl_info = {
    "name":         "GBXPosBlender",
    "author":       "DarkMattrMaestro",
    "description":  "An addon to bring Trackmania Nations Forever to Blender and inversely.",
    "blender":      (2, 80, 0),
    "version":      (0, 0, 2),
    "location":     "",
    "warning":      "",
    "category":     "",
}

import sys, os, bpy

from . import (
    importing,
    loading,
    exporting,
    python_cs_interface,
    utils,
)

modules = (
    importing,
    loading,
    exporting,
    python_cs_interface,
    utils,
)

# sys.path.append(os.path.dirname(__file__))

def register():
    for module in modules:
        module.register()


def unregister():
    for module in reversed(modules):
        module.unregister()