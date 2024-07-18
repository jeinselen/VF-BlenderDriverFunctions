bl_info = {
	"name": "VF Driver wiggle",
	"author": "John Einselen - Vectorform LLC",
	"version": (0, 1),
	"blender": (2, 83, 0),
	"location": "Channel driver -> wiggle(2, 0.5, 1, 2.5)",
	"description": "Adds wiggle(frequency, amplitude, octaves, seed) driver function",
	"warning": "inexperienced developer, use at your own risk",
	"doc_url": "https://github.com/jeinselenVF/VF-BlenderDriverFunctions",
	"tracker_url": "https://github.com/jeinselenVF/VF-BlenderDriverFunctions/issues",
	"category": "Rigging"}

# Thanks for the help:
#	https://blender.stackexchange.com/questions/71305/how-to-make-an-addon-with-custom-driver-function

# Example usage:
#	wiggle(2, 2, 5)
#	this is vaguely comparable to AE's 2 wiggles per second with 2 octaves and a random seed of 5

import bpy
from bpy.app.handlers import persistent
from bpy.app import driver_namespace as dns
from mathutils import noise

def wiggle(freq, amp, oct, seed):
	time = bpy.context.scene.frame_current / bpy.context.scene.render.fps
	pos = (time*0.73*freq, time*0.53*freq, seed) # magic numbers to try and mimic the actually-faster-than-per-second wiggle value in AE
	return noise.fractal(pos, 1.0, 2.0, oct, noise_basis='PERLIN_ORIGINAL') * amp

@persistent
def load_handler(dummy):
	dns = bpy.app.driver_namespace
	dns["wiggle"] = wiggle

def register():
	load_handler(None)
	bpy.app.handlers.load_post.append(load_handler)

def unregister():
	bpy.app.handlers.load_post.remove(load_handler)

if __name__ == "__main__":
	register()