bl_info = {
	"name": "VF Driver HSV",
	"author": "John Einselen - Vectorform LLC",
	"version": (0, 1),
	"blender": (2, 80, 0),
	"location": "Channel driver -> hsv(0.1, 0.5, 1.0, 0)",
	"description": "Adds hsv(hue, saturation, value, RGB channel output) driver function",
	"warning": "inexperienced developer, use at your own risk",
	"wiki_url": "",
	"tracker_url": "",
	"category": "Rigging"}

# Thanks for the help:
#	https://blender.stackexchange.com/questions/71305/how-to-make-an-addon-with-custom-driver-function
#	https://blender.stackexchange.com/questions/80034/hsv-to-rgb-conversion

# Example usage:
#	hsv2r(0.5, 1, 1, 0)
#	this will convert HSV input values into RGB output values, and return the first (red) channel

import bpy
from colorsys import hsv_to_rgb
from bpy.app.handlers import persistent
from bpy.app import driver_namespace as dns

def hsv(h, s, v, c):
	color = hsv_to_rgb(h, s, v)
	if c < 0.5:
		return color[0]
	elif c < 1.5:
		return color[1]
	else:
		return color[2]

@persistent
def load_handler(dummy):
	dns = bpy.app.driver_namespace
	dns["hsv"] = hsv

def register():
	load_handler(None)
	bpy.app.handlers.load_post.append(load_handler)

def unregister():
	bpy.app.handlers.load_post.remove(load_handler)

if __name__ == "__main__":
	register()
