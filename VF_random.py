bl_info = {
	"name": "VF Driver random",
	"author": "John Einselen - Vectorform LLC",
	"version": (0, 1),
	"blender": (2, 80, 0),
	"location": "Channel driver -> random(-0.5, 1.5, 10)",
	"description": "Adds random(minimum, maximum, seed) driver function",
	"warning": "inexperienced developer, use at your own risk",
	"wiki_url": "",
	"tracker_url": "",
	"category": "Rigging"}

# Thanks for the help:
#	https://blender.stackexchange.com/questions/71305/how-to-make-an-addon-with-custom-driver-function

# Example usage:
#	random(-0.5, +1.5, 10)
#	random(-1.5, +1.5)
#	The seed value is not required, but without it, will return a random value literally every time the driver is accessed (perhaps useful for jittering something?)

import bpy
from bpy.app.handlers import persistent
from bpy.app import driver_namespace as dns
from random import random as rand, seed

def vf_random(a, b, s=-1):
	if s >= 0:
		seed(int(s))
	return (rand() * (b - a)) + a

@persistent
def load_handler(dummy):
	dns = bpy.app.driver_namespace
	dns["random"] = vf_random

def register():
	load_handler(None)
	bpy.app.handlers.load_post.append(load_handler)

def unregister():
	bpy.app.handlers.load_post.remove(load_handler)

if __name__ == "__main__":
	register()
