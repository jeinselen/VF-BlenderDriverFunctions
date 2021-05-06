bl_info = {
	"name": "VF curveAtTime",
	"author": "John Einselen - Vectorform LLC",
	"version": (0, 2),
	"blender": (2, 80, 0),
	"location": "Channel driver -> curveAtTime(\"Cube\", 0, frame-5)",
	"description": "Adds curveAtTime(objectName, curveIndex, time) driver function",
	"warning": "inexperienced developer, use at your own risk",
	"wiki_url": "",
	"tracker_url": "",
	"category": "Rigging"}

# Thanks for the help:
#	https://blenderartists.org/t/read-object-properties-from-a-specific-frame/531238/2
#	https://blender.stackexchange.com/questions/71305/how-to-make-an-addon-with-custom-driver-function

# Example usage:
#	curveAtTime("Cube", 0, frame-5)
#	returns the "Cube" object's first animation curve value 5 frames in the past
#	note that Blender requires an animation curve to get time-based data, and doesn't reference them by type or name, only index number

import bpy
from bpy.app.handlers import persistent
from bpy.app import driver_namespace as dns

def curve_at_time(name, channel, frame):
	obj = bpy.data.objects[name]
	fcurve = obj.animation_data.action.fcurves[channel]
	return fcurve.evaluate(frame)

@persistent
def load_handler(dummy):
	dns = bpy.app.driver_namespace
	dns["curveAtTime"] = curve_at_time

def register():
	load_handler(None)
	bpy.app.handlers.load_post.append(load_handler)

def unregister():
	bpy.app.handlers.load_post.remove(load_handler)

if __name__ == "__main__":
	register()
