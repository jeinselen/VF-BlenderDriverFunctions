bl_info = {
	"name": "VF Driver Functions",
	"author": "John Einselen - Vectorform LLC",
	"version": (0, 3),
	"blender": (2, 83, 0),
	"location": "Channel driver > curveAtTime(), hsv(), wiggle()",
	"description": "Adds curveAtTime(), hsv(), wiggle() driver functions",
	"warning": "inexperienced developer, use at your own risk",
	"doc_url": "https://github.com/jeinselenVF/VF-BlenderDriverFunctions",
	"tracker_url": "https://github.com/jeinselenVF/VF-BlenderDriverFunctions/issues",
	"category": "Rigging"}

import bpy
from bpy.app.handlers import persistent
from colorsys import hsv_to_rgb
from mathutils import noise



# Example:
#	curveAtTime(item name, animation curve index, sample time in frames)
#	curveAtTime("Cube", 0, frame-5)
#	returns the "Cube" object's first animation curve value 5 frames in the past
#	Blender requires an animation curve to get non-current-frame data
#	Blender doesn't reference animation curves by type or name, only numerical index

def curve_at_time(name, channel, frame):
	obj = bpy.data.objects[name]
	fcurve = obj.animation_data.action.fcurves[channel]
	return fcurve.evaluate(frame)



# Example:
#	hsv(hue, saturation, value, output channel)
#	hsv(0.5, 1, 1, 0)
#	This will convert HSV input values into RGB output values, returning the first (red) channel

def hsv(h, s, v, c):
	color = hsv_to_rgb(h, s, v)
	if c < 0.5:
		return color[0]
	elif c < 1.5:
		return color[1]
	else:
		return color[2]



# Example:
#	wiggle(speed, distance, octaves, seed)
#	wiggle(2, 1, 3, 4)
#	This is vaguely comparable to AE's 2 wiggles per second moving a distance of 1m with 3 octaves and a random seed of 4

def wiggle(freq, amp, oct, seed):
	time = bpy.context.scene.frame_current / bpy.context.scene.render.fps
	pos = (time*0.73*freq, time*0.53*freq, seed) # magic numbers to try and mimic the actually-faster-than-per-second wiggle value in AE
	return noise.fractal(pos, 1.0, 2.0, oct, noise_basis='PERLIN_ORIGINAL') * amp



# Driver registration
#	Blender will fail to load custom drivers when re-opening a project
#	Everything still works, but every channel that uses a custom driver must be selected/deselected or refresh some other way before the calculations will update
#	No known fix...maybe a long-standing limitation of Blender driver evaluation?

@persistent
def vf_driver_functions(dummy):
	dns = bpy.app.driver_namespace
	dns["curveAtTime"] = curve_at_time
	dns["hsv"] = hsv
	dns["wiggle"] = wiggle

def register():
	vf_driver_functions(None)
	bpy.app.handlers.load_post.append(vf_driver_functions)

def unregister():
	bpy.app.handlers.load_post.remove(vf_driver_functions)

if __name__ == "__main__":
	register()